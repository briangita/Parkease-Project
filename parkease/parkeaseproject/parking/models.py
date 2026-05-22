from django.db import models
from django.utils import timezone
from decimal import Decimal
import uuid


class Parking(models.Model):
    VEHICLE_TYPES = [
        ("truck", "Truck"),
        ("personal_car", "Personal Car"),
        ("taxi", "Taxi"),
        ("coaster", "Coaster"),
        ("boda_boda", "Boda-boda"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    driver_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    number_plate = models.CharField(max_length=10)
    vehicle_model = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    nin_number = models.CharField(max_length=20, blank=True, null=True)

    arrival_time = models.DateTimeField(default=timezone.now)
    receipt_number = models.CharField(max_length=30, unique=True, blank=True)

    signed_out = models.BooleanField(default=False)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_phone = models.CharField(max_length=15, blank=True, null=True)
    receiver_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    receiver_nin = models.CharField(max_length=20, blank=True, null=True)
    exit_time = models.DateTimeField(blank=True, null=True)

    parking_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = "PK-" + str(uuid.uuid4()).split("-")[0].upper()
        super().save(*args, **kwargs)

    def calculate_fee(self):
        end_time = self.exit_time or timezone.now()
        duration = end_time - self.arrival_time
        hours = duration.total_seconds() / 3600
        arrival_hour = self.arrival_time.hour

        is_day = 6 <= arrival_hour <= 18

        if self.vehicle_type == "truck":
            return 2000 if hours < 3 else 5000 if is_day else 10000

        if self.vehicle_type in ["personal_car", "taxi"]:
            return 2000 if hours < 3 else 3000 if is_day else 2000

        if self.vehicle_type == "coaster":
            return 3000 if hours < 3 else 4000 if is_day else 2000

        if self.vehicle_type == "boda_boda":
            return 1000 if hours < 3 else 2000

        return 0

    def __str__(self):
        return f"{self.number_plate} - {self.driver_name}"