from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = "__all__"


class updateForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = [
            "firstname",
            "lastname",
            "username",
            "password",
            "mobile",
            "city",
            "state",
            "photo",
        ]


class notedForm(forms.ModelForm):
    class Meta:
        model = noteSubmit
        fields = ["title", "desc", "notefile"]
