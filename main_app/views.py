import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Transaction
from django.contrib import messages
from customer.models import Customer
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime

from datetime import datetime

def landing_page(request):
    return render(request, "main_app/landing_page.html")

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

    context = {
        "car": car
    }

    return render(request, "main_app/car_detail.html", context)


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
    transaction = Transaction.objects.get(pk=transaction_id)
    car = transaction.car

    if request.method == "POST":
        car.status = "available"
        car.save()
        transaction.delete()
        messages.info(request, "You've successfully deleted transaction")
        return redirect("transaction_detail")
    
    context = {
        "transaction": transaction
    }

    return render(request, "main_app/delete_transaction.html", context)

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
    