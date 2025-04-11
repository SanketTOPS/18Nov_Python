from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail, send_mass_mail
from FinalProject import settings
import random
import json
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "index.html")


def signin(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = userSignup.objects.filter(username=username, password=password)
        userid = userSignup.objects.get(username=username)
        print("Current User:", userid.id)
        if user:  # TRUE
            print("Login Successfull!")
            request.session["user"] = username  # generate a session
            request.session["userid"] = userid.id
            return redirect("notes")
        else:
            print("Error!Login Faild...")
            msg = "Error!Login Faild..."
    return render(request, "signin.html", {"msg": msg})


def signup(request):
    msg = ""
    global newuser
    if request.method == "POST":
        newuser = signupForm(request.POST, request.FILES)
        username = ""
        if newuser.is_valid():
            try:
                username = newuser.cleaned_data.get("username")
                userSignup.objects.get(username=username)
                msg = "Error!Username is already exists..."
            except userSignup.DoesNotExist:
                # OTP Email Sending
                newuser.save()
                global otp
                otp = random.randint(1111, 9999)
                sub = "Verify your account!"
                mmsg = f"Hello User\n\nThank you for registraion with us!\nYour account verification code is {otp}.\n\nThanks & Regards\nSanket Chauhan | TOPS Tech-Rajkot\n+91 9724799469 | sanket.tops@gmail.com"
                from_email = settings.EMAIL_HOST_USER
                to_email = [request.POST.get("username")]
                send_mail(
                    subject=sub,
                    message=mmsg,
                    from_email=from_email,
                    recipient_list=to_email,
                )
                msg = "Email OTP sent, Please verify your account"
                # return redirect("otpverify")
                return redirect("signin")
        else:
            print(newuser.errors)
    return render(request, "signup.html", {"msg": msg})


def notes(request):
    msg = ""
    user = request.session.get("user")
    username = userSignup.objects.get(username=user)
    if request.method == "POST":
        form = notedForm(request.POST, request.FILES)
        if form.is_valid():
            cuser = form.save(commit=False)
            cuser.submitted_at = datetime.now()
            cuser.status = "Pending"
            cuser.user = username
            cuser.save()
            print("Your notes has been submitted!")
            msg = "Your notes has been submitted!"
            return redirect("notes")
        else:
            print(form.errors)
    return render(request, "notes.html", {"user": user, "msg": msg})


def profile(request):
    msg = ""
    user = request.session.get("user")
    userid = request.session.get("userid")
    cuser = userSignup.objects.get(id=userid)
    if request.method == "POST":
        updatereq = updateForm(request.POST, request.FILES, instance=cuser)
        if updatereq.is_valid():
            updatereq.state = request.POST.get("state") or updatereq.state
            updatereq.save()
            print("Your profile has been updated!")
            msg = "Your profile has been updated!"
            return redirect("profile")
        else:
            print(updatereq.errors)
    return render(
        request,
        "profile.html",
        {"user": user, "cuser": cuser, "msg": msg},
    )


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def userlogut(request):
    logout(request)
    return redirect("signin")


def otpverify(request):
    global otp
    msg = ""

    print("OTP:", otp)

    if request.method == "POST":
        if request.POST["otp"] == str(otp):
            msg = "Verification Successfull!"
            return redirect("signin")
        else:
            msg = "Invalid OTP. Please try again."

    return render(request, "otpverify.html", {"msg": msg})
