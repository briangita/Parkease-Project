from django import forms
from .models import Parking
import re


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = [
            "driver_name",
            "vehicle_type",
            "number_plate",
            "vehicle_model",
            "vehicle_color",
            "phone_number",
            "nin_number",
        ]

        widgets = {
            "driver_name": forms.TextInput(attrs={"class": "form-control"}),
            "vehicle_type": forms.Select(attrs={"class": "form-control"}),
            "number_plate": forms.TextInput(attrs={"class": "form-control"}),
            "vehicle_model": forms.TextInput(attrs={"class": "form-control"}),
            "vehicle_color": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "nin_number": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_driver_name(self):
        name = self.cleaned_data.get("driver_name")
        if not name[0].isupper() or any(char.isdigit() for char in name):
            raise forms.ValidationError("Name must start with a capital letter and contain no numbers.")
        return name

    def clean_number_plate(self):
        plate = self.cleaned_data.get("number_plate").upper()
        if not plate.startswith("U") or not plate.isalnum() or len(plate) != 7:
            raise forms.ValidationError("Number plate must start with U, be alphanumeric, and be exactly 7 characters long.")
        return plate

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if not re.match(r"^(07|03)\d{8}$", phone):
            raise forms.ValidationError("Enter a valid Ugandan phone number.")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        vehicle_type = cleaned_data.get("vehicle_type")
        nin_number = cleaned_data.get("nin_number")

        if vehicle_type == "boda_boda" and not nin_number:
            raise forms.ValidationError("NIN number is required for boda-bodas.")

        return cleaned_data


class SignOutForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = [
            "receiver_name",
            "receiver_phone",
            "receiver_gender",
            "receiver_nin",
        ]

        widgets = {
            "receiver_name": forms.TextInput(attrs={"class": "form-control"}),
            "receiver_phone": forms.TextInput(attrs={"class": "form-control"}),
            "receiver_gender": forms.Select(attrs={"class": "form-control"}),
            "receiver_nin": forms.TextInput(attrs={"class": "form-control"}),
        }