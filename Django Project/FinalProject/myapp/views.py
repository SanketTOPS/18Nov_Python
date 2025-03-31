from django.shortcuts import render
from .forms import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def signin(request):
    return render(request, "signin.html")


def signup(request):
    if request.method == "POST":
        newuser = signupForm(request.POST, request.FILES)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
        else:
            print(newuser.errors)
    return render(request, "signup.html")


def notes(request):
    return render(request, "notes.html")


def profile(request):
    return render(request, "profile.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
