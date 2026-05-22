from django.urls import path
from . import views

urlpatterns = [
    path("battery_form/", views.battery_service_form, name="battery_service_form"),
    path("list/", views.battery_service_list, name="battery_service_list"),
    path("receipt/<int:pk>/", views.battery_receipt, name="battery_receipt"),
    path("report/", views.battery_report, name="battery_report"),
]