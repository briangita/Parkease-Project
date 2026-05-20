from django.urls import path
from web import views

urlpatterns = [
    path('',views.parking_list, name='parking_list'),
    path('add/',views.add_parking, name='add_parking'),
]