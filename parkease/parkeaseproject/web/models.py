from django.db import models

# Create your models here.

class Parking(models.Model):
     vehicle_number = models.CharField(max_length=20)
     vehicle_type = models.CharField(max_length=50)
     owner_name = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=15)
     parking_slot = models.CharField(max_length=20)
     entry_time = models.DateTimeField()
     exit_time = models.DateTimeField(blank=True, null=True)
     signed_out = models.BooleanField(default=False)
