from django.contrib import admin
from .models import *

# Register your models here.
class billData(admin.ModelAdmin):
    list_display=["id","name","qty","price","total"]

admin.site.register(mybill,billData)
