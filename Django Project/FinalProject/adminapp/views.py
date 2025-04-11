from django.shortcuts import render, redirect
from myapp.models import *


# Create your views here.


def admin_login(request):
    msg = ""
    if request.method == "POST":
        username = "admin"
        password = "Tops@123"
        if (
            request.POST["username"] == username
            and request.POST["password"] == password
        ):
            print("Login successfull!")
            return redirect("admin_home")
        else:
            msg = "Login Faild...Try again!"
    return render(request, "admin_login.html", {"msg": msg})


def admin_home(request):
    return render(request, "admin_home.html")


def admin_userdata(request):
    users = userSignup.objects.all()
    return render(request, "admin_userdata.html", {"users": users})


def admin_notesdata(request):
    allnotes = noteSubmit.objects.all()
    return render(request, "admin_notesdata.html", {"allnotes": allnotes})
