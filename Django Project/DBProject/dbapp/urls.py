from django.contrib import admin
from django.urls import path, include
from dbapp import views

urlpatterns = [
    path("", views.index),
    path("showdata/", views.showdata, name="showdata"),
    path("deletedata/<int:id>", views.deletedata),
    path("updatedata/<int:id>", views.updatedata),
    path("delete_id/", views.delete_id),
]
