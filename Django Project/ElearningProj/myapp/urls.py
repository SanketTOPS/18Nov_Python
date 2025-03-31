from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("team/", views.team),
    path("courses/", views.courses),
    path("testimonial/", views.testimonial),
]
