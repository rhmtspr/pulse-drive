from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from customer.models import Customer

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    message = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            message = "login Success"
            messages.success(request, message)
            return redirect('/')
        else:
            message = 'login failed'
            messages.error(request, message)
    return render(request, "login.html")

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    message = ''
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            user = User.objects.filter(username=username)
            if user.count() == 0:
                new_user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    is_active=True
                )
                new_user.set_password(password1)
                new_user.save()

                customer = Customer.objects.create(
                    user=new_user,
                    fullname=f"{first_name} {last_name}"
                )

                customer.save()

                message = "Register Success"
                messages.success(request, message)
                return redirect('/')
            else:
                message = 'username sudah digunakan'
        else:
            message = 'password tidak sama'
    
    messages.error(request, message)

    return render(request, "signup.html")

def logout_account(request):
    logout(request)
    return redirect('/')