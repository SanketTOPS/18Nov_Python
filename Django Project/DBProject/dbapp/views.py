from django.shortcuts import render, redirect
from .forms import *
import dbapp.temp as temp


# Create your views here.
def index(request):
    if request.method == "POST":  # TRUE
        newuser = userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Record inserted!")
        else:
            print(newuser.errors)
    return render(request, "index.html")


def showdata(request):
    stdata = userinfo.objects.all()  # fetch the all data from model
    return render(request, "showdata.html", {"stdata": stdata})


def deletedata(request, id):
    stid = userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect("showdata")
