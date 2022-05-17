from django import forms
from .models import Number, Password


class NumberForm(forms.ModelForm):

    class Meta:
        model = Number
        fields = ("profile", "numbers", "columns")


class PasswordForm(forms.ModelForm):

    class Meta:
        model = Password
        fields = ("profile", "password")
