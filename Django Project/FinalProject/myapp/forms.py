from django import forms
from .models import *


STATE_CHOICES = (
    ("Gujarat", "Gujarat"),
    ("Delhi", "Delhi"),
    ("Punjab", "Punjab"),
    ("Other", "Other"),
)


class signupForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = "__all__"


class updateForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATE_CHOICES, required=False)

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


class contactForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = "__all__"
