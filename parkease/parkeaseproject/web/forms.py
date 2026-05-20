from django import forms
from .models import Parking

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = "__all__"
        widgets = {
             "vehicle_number": forms.TextInput(attrs={ "class": "form-control", "placeholder": "Enter vehicle number" }),
             "vehicle_type": forms.TextInput(attrs={ "class": "form-control" }),
             "owner_name": forms.TextInput(attrs={ "class": "form-control", "placeholder": "Enter owner name" }),
             "phone_number": forms.TextInput(attrs={ "class": "form-control", "placeholder": "Enter phone number" }), 
             "parking_slot": forms.TextInput(attrs={ "class": "form-control", "placeholder": "Enter parking slot" }),
             "entry_time": forms.DateTimeInput(attrs={ "class": "form-control", "type": "datetime-local" }),
             "exit_time": forms.DateTimeInput(attrs={ "class": "form-control", "type": "datetime-local" }),
             "signed_out": forms.CheckboxInput(attrs={ "class": "form-check-input" }),
               }

