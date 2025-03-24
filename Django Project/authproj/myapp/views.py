from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.


def index(request):
    if request.method == "POST":
        unm = request.POST["username"]
        pas = request.POST["password"]

        user = userSignup.objects.filter(username=unm, password=pas)
        if user:  # TRUE
            print("Login Successfull!")
            request.session["user"] = unm  # generate a session
            return redirect("home")
        else:
            print("Error!Login Faild...")
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        newuser = signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect("/")
        else:
            print(newuser.errors)
    return render(request, "signup.html")


def home(request):
    user = request.session.get("user")
    return render(request, "home.html", {"user": user})


def userlogut(request):
    logout(request)
    return redirect("/")
