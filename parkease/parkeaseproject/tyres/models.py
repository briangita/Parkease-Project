from django.db import models

# Create your models here.

class TyreService(models.Model):
    SERVICE_CHOICES = [
        ('pressure_check', 'Pressure Check'),
        ('puncture_repair', 'Puncture Repair'),
        ('tyre_replacement', 'Tyre Replacement'),
        ('valve_replacement', 'Valve Replacement'),
        ('wheel_balancing', 'Wheel Balancing'),
    ]

    customer_name = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    tyre_size = models.CharField(max_length=20)
    tyre_model = models.CharField(max_length=50)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

