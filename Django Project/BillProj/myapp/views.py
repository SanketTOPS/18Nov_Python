from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method=="POST":
        newbill=billForm(request.POST)
        nm=request.POST["name"]
        qty=request.POST["qty"]
        pri=request.POST["price"]
        total=int(qty)*int(pri)
        if newbill.is_valid():
            bdata=mybill(name=nm,qty=qty,price=pri,total=total)
            bdata.save()
            print("Bill Geerated!")
        else:
            pri("Error!")
    return render(request,'index.html')