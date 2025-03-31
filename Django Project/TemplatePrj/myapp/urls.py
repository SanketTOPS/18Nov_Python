from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index),
    path("about/",views.about),
    path("contact/",views.contact),
    path("gallery/",views.gallery),
    path("services/",views.services),
]
