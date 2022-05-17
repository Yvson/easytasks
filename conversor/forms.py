from django import forms
from .models import Conversion


class ConversionForm(forms.ModelForm):

    class Meta:
        model = Conversion
        fields = ("profile", "unit_from", "unit_to")
