from django.urls import path
from . import views

urlpatterns = [
    path('', views.tyre_service_list, name='tyre_service_list'),
    path('form/', views.tyre_service_form, name='tyre_service_form'),
    path('receipt/<int:pk>/', views.tyre_service_receipt, name='tyre_service_receipt'),
    path('report/', views.tyre_service_report, name='tyre_service_report'),
]