from django.urls import path

from parking import views

urlpatterns = [    
    path("parkingform/", views.parking_form, name="parking_form"),
    path('parkinglist', views.parking_list, name="parking_list"),
    path("edit/<int:pk>/", views.parking_edit, name="parking_edit"),
    path("delete/<int:pk>/", views.parking_delete, name="parking_delete"),
    path("receipt/<int:pk>/", views.parking_receipt, name="parking_receipt"),
    path("sign-out/<int:pk>/", views.sign_out_parking, name="sign_out_parking"),
    path("report/", views.parking_report, name="parking_report"),
]