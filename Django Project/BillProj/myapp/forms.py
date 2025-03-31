from django import forms
from .models import *

class billForm(forms.ModelForm):
    class Meta:
        model=mybill
        fields=["name","qty","price"]