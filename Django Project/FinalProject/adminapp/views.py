from django.shortcuts import render, redirect

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
