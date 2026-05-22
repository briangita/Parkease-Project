from django import forms
from .models import BatteryService


class BatteryServiceForm(forms.ModelForm):
    class Meta:
        model = BatteryService
        fields = [
            "customer_name",
            "phone_number",
            "number_plate",
            "service_type",
            "battery_type",
            "service_fee",
        ]

        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "number_plate": forms.TextInput(attrs={"class": "form-control"}),
            "service_type": forms.Select(attrs={"class": "form-control"}),
            "battery_type": forms.TextInput(attrs={"class": "form-control"}),
            "service_fee": forms.NumberInput(attrs={"class": "form-control"}),
        }