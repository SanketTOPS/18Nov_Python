from django.contrib import admin
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path("", views.admin_login),
    path("admin_home/", views.admin_home, name="admin_home"),
]
