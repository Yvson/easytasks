from django.forms import ModelForm
from .models import Color


class ColorForm(ModelForm):

    class Meta:
        model = Color
        fields = ("profile", "color")
