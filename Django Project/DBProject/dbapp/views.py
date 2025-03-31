from django.shortcuts import render, redirect
from .forms import *
import dbapp.temp as tp


# Create your views here.
def index(request):
    tp.getnum()
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


def updatedata(request, id):
    stid = userinfo.objects.get(id=id)
    print("Selected ID:", stid)
    if request.method == "POST":
        update = updateForm(request.POST, instance=stid)
        if update.is_valid():
            update.save()
            print("Record Updated!")
            return redirect("showdata")
        else:
            print("Error!Record not update")
    return render(request, "updatedata.html", {"stid": stid})


def delete_id(request):
    msg = ""
    if request.method == "POST":
        stid = request.POST["id"]
        try:
            id = userinfo.objects.get(id=stid)
            userinfo.delete(id)
        except userinfo.DoesNotExist:
            print("ID not found...")
    return render(request, "delete_id.html")
