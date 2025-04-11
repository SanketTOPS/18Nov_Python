from django.contrib import admin
from django.urls import path
from adminapp import views

urlpatterns = [
    path("", views.admin_login),
    path("admin_home/", views.admin_home, name="admin_home"),
    path("admin_userdata/", views.admin_userdata, name="admin_userdata"),
    path("admin_notesdata/", views.admin_notesdata, name="admin_notesdata"),
]
