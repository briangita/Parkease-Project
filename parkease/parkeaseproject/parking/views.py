from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Sum
from .models import Parking
from .forms import ParkingForm, SignOutForm
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required


@login_required
def parking_form(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("parking_list")
    else:
        form = ParkingForm()

    return render(request, "parking_form.html", {"form": form})

@login_required
def parking_list(request):
    parkings = Parking.objects.all().order_by("-arrival_time")
    return render(request, "parking_list.html", {"parkings": parkings})

@login_required
def parking_edit(request, pk):
    parking = get_object_or_404(Parking, pk=pk)

    if request.method == "POST":
        form = ParkingForm(request.POST, instance=parking)
        if form.is_valid():
            form.save()
            return redirect("parking_list")
    else:
        form = ParkingForm(instance=parking)

    return render(request, "parking_form.html", {"form": form})

@login_required
@admin_required
def parking_delete(request, pk):
    parking = get_object_or_404(Parking, pk=pk)

    if request.method == "POST":
        parking.delete()
        return redirect("parking_list")

    return render(request, "parking_delete.html", {"parking": parking})

@login_required 
def parking_receipt(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    return render(request, "parking_receipt.html", {"parking": parking})

@login_required
def sign_out_parking(request, pk):
    parking = get_object_or_404(Parking, pk=pk)

    if request.method == "POST":
        form = SignOutForm(request.POST, instance=parking)
        if form.is_valid():
            parking = form.save(commit=False)
            parking.signed_out = True
            parking.exit_time = timezone.now()
            parking.parking_fee = parking.calculate_fee()
            parking.save()
            return redirect("parking_receipt", pk=parking.pk)
    else:
        form = SignOutForm(instance=parking)

    return render(request, "sign_out.html", {"form": form, "parking": parking})

@login_required
@admin_required
def parking_report(request):
    today = timezone.now().date()

    parkings = Parking.objects.filter(
        signed_out=True,
        exit_time__date=today
    ).order_by("-exit_time")

    total_revenue = parkings.aggregate(total=Sum("parking_fee"))["total"] or 0

    return render(request, "parking_report.html", {
        "parkings": parkings,
        "total_revenue": total_revenue,
        "today": today,
    })