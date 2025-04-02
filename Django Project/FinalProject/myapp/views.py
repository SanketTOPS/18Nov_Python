from django.shortcuts import render, redirect
from .forms import *

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
                username = newuser.cleaned_data.get(username=username)
                print("Username is already exists!")
                msg = "Username is already exists!"
            except userSignup.DoesNotExist:
                newuser.save()
                print("Signup Successfully!")
                return redirect("signin")
        else:
            print(newuser.errors)
    return render(request, "signup.html", {"msg": msg})


def notes(request):
    return render(request, "notes.html")


def profile(request):
    return render(request, "profile.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
