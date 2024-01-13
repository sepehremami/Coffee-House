from django import forms
from .models import Order


class StatusFormSet(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["status"]
