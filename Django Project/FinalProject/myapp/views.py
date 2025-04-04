from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail, send_mass_mail
from FinalProject import settings
import random

# Create your views here.


def index(request):
    return render(request, "index.html")


def signin(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = userSignup.objects.filter(username=username, password=password)
        if user:  # TRUE
            print("Login Successfull!")
            request.session["user"] = username  # generate a session
            return redirect("notes")
        else:
            print("Error!Login Faild...")
            msg = "Error!Login Faild..."
    return render(request, "signin.html", {"msg": msg})


def signup(request):
    msg = ""
    if request.method == "POST":
        newuser = signupForm(request.POST, request.FILES)
        username = ""
        if newuser.is_valid():
            try:
                username = newuser.cleaned_data.get("username")
                userSignup.objects.get(username=username)
                print("Username is already exists!")
                msg = "Username is already exists!"
            except userSignup.DoesNotExist:
                newuser.save()
                print("Signup Successfully!")

                # Email Sending Code

                otp = random.randint(11111, 99999)
                sub = "Verify your account"
                msg = f"Hello User!\n\nThank you for registraion with us!\nYour account has been created!\n\nYour one time password is {otp}.\n\nThanks & Regards\nTOPS Technologies\n+919724799469 | sanket.tops@gmail.com"
                from_ID = settings.EMAIL_HOST_USER
                to_ID = [request.POST.get("username")]
                send_mail(
                    subject=sub, message=msg, from_email=from_ID, recipient_list=to_ID
                )
                return redirect("otpverify")
        else:
            print(newuser.errors)
    return render(request, "signup.html", {"msg": msg})


def notes(request):
    user = request.session.get("user")
    return render(request, "notes.html", {"user": user})


def profile(request):
    return render(request, "profile.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def userlogut(request):
    logout(request)
    return redirect("signin")


def otpverify(request):
    return render(request, "otpverify.html")
