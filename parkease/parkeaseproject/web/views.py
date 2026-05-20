from django.shortcuts import render, redirect
from .models import Parking
from .forms import ParkingForm

def parking_list(request): 
    parkings = Parking.objects.all()
    
    return render(request, 'parking_list.html', { 'parkings': parkings })

def add_parking(request):
     
     if request.method == "POST":  
         form = ParkingForm(request.POST)
         if form.is_valid(): 
             form.save()
             return redirect('parking_list')
     else:
         form = ParkingForm()

     return render(request, 'add_parking.html', { 'form': form })