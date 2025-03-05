from django.shortcuts import render
import random


# Create your views here.
n=1
def index(request):
    global n
    n+=1
    name="HItesh"
    num=random.randint(1111,9999)
    return render(request, "index.html",{'nm':name,'num':num,'n':n})
