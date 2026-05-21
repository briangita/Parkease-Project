from django import forms
from .models import TyreService

class TyreServiceForm(forms.ModelForm):
    class Meta:
        model = TyreService
        fields = [
            'customer_name',
            'number_plate',
            'phone_number',
            'tyre_size',
            'tyre_model',
            'service_type',
            'service_fee',
            
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'number_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tyre_size': forms.TextInput(attrs={'class': 'form-control'}),
            'tyre_model': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'service_fee': forms.NumberInput(attrs={'class': 'form-control'}),
        }