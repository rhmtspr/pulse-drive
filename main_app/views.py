from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Transaction, Reviews
from django.contrib import messages
from customer.models import Customer
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime

from datetime import datetime

@login_required
def home(request):
    cars = Car.objects.all()

    context = {
        "cars": cars
    }

    return render(request, 'main_app/index.html', context)

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    reviews = Reviews.objects.filter(car=car)

    if request.method == "POST":
        review_content = request.POST.get("review")
        review_obj = Reviews.objects.create(
            user=request.user,
            car=car,
            content=review_content
        )

        review_obj.save()

        messages.success(request, "Review has been created")

        return redirect("car_detail", car_id=car_id)

    context = {
        "car": car,
        "reviews": reviews,

    }

    return render(request, "main_app/car_detail.html", context)

@login_required
def user_reviews(request):
    reviews = Reviews.objects.filter(user=request.user)

    context = {
        "reviews": reviews
    }

    return render(request, "main_app/user_reviews.html", context)

@login_required
def delete_review(request, review_id):
    try:
        review = Reviews.objects.get(id=review_id)
        review.delete()
        return redirect("user_reviews")
    except:
        return HttpResponseNotFound("Review not found")

@login_required
def create_transaction(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == "POST":
        rental_price = request.POST.get("rentalprice")
        rental_date_input = request.POST.get("rentaldate")
        return_date_input = request.POST.get("returndate")

        format_in = "%m/%d/%Y %I:%M %p"
        format_out = "%Y-%m-%d %H:%M:%S"

        rental_date_data = datetime.strptime(rental_date_input, format_in)
        return_date_data = datetime.strptime(return_date_input, format_in)

        formatted_rental_date = rental_date_data.strftime(format_out)
        formatted_return_date = return_date_data.strftime(format_out)

        transaction = Transaction.objects.create(
            user=request.user,
            car=car,
            rental_price=rental_price,
            rental_date=formatted_rental_date,
            return_date=formatted_return_date
        )

        car.status = "unavailable"
        car.save()

        transaction.save()

        messages.success(request, "transaction has been created")

    context = {
        "car": car,
    }

    return render(request, "main_app/create_transaction.html", context)

@login_required
def transaction_detail(request):
    transactions = Transaction.objects.filter(user=request.user)

    total_price = sum([transaction.rental_price for transaction in transactions])

    context = {
        "transactions": transactions,
        "total_price": total_price
    }

    return render(request, "main_app/transaction_detail.html", context)

@login_required
def delete_transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        car = transaction.car
        car.status = "available"
        car.save()
        transaction.delete()
        return redirect("transaction_detail")
    except:
        return HttpResponseNotFound("Transaction not found")

@login_required
def generate_bill(request):
    transactions = Transaction.objects.filter(user=request.user)
    username = Customer.objects.get(user=request.user).fullname.title()
    total_price = sum([transaction.rental_price for transaction in transactions])
    current_date = datetime.now()

    context = {
        "username": username,
        "transactions": transactions,
        "total_price": total_price,
        "current_date": current_date
    }

    return render(request, "main_app/generate_bill.html", context)

@login_required
def pdf_report_create(request):
    transactions = Transaction.objects.filter(user=request.user)
    username = Customer.objects.get(user=request.user).fullname.title()
    total_price = sum([transaction.rental_price for transaction in transactions])
    current_date = datetime.now()

    template_path = "main_app/pdf_report.html"

    context = {
        "username": username,
        "transactions": transactions,
        "total_price": total_price,
        "current_date": current_date
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse("We had some errors <pre> " + html + "</pre>")
    return response
    