from django.contrib import admin
from .models import *

# Register your models here.


class studData(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "name", "email", "dob", "mobile", "address"]


admin.site.register(userinfo, studData)
