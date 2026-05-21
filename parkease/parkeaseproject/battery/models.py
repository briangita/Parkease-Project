from django.db import models

# Create your models here.

class BatteryService(models.Model):
    SERVICE_CHOICES = [
        ('hiring', 'Hiring'),
        ('buying', 'Buying'),
    ]

    customer_name = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    battery_type = models.CharField(max_length=50)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
