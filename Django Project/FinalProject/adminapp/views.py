from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
from django.core.mail import send_mail
from datetime import datetime
from FinalProject import settings


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


def approved_note(request, id):
    note = get_object_or_404(noteSubmit, id=id)
    note.status = "Approved"
    note.approved_at = datetime.now()
    note.save()
    print("Notes approved!")

    # Send Email
    sub = "Your Notes has been Approved!"
    msg = f"Hello {note.user.firstname}\n\nYour notes has been approved by Admin.\n\nThanks & Regards\nAdmin - NotesApp\nTOPS Technologies\n+91 9724799469 | sanket.tops@gmail.com"
    from_email = settings.EMAIL_HOST_USER
    to_email = [note.user.username]
    send_mail(subject=sub, message=msg, from_email=from_email, recipient_list=to_email)
    print("Email sent successfully!")

    return redirect("admin_notesdata")


def rejected_note(request, id):
    note = get_object_or_404(noteSubmit, id=id)
    note.status = "Rejected"
    note.approved_at = datetime.now()
    note.save()
    print("Notes Rejected!")
    return redirect("admin_notesdata")
