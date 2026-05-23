from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import BatteryService
from .forms import BatteryServiceForm
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required


@login_required
def battery_service_form(request):
    if request.method == "POST":
        form = BatteryServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("battery_service_list")
    else:
        form = BatteryServiceForm()

    return render(request, "battery_service_form.html", {"form": form})

@login_required
def battery_service_list(request):
    services = BatteryService.objects.all().order_by("-date_time")
    return render(request, "battery_service_list.html", {"services": services})

@login_required
def battery_receipt(request, pk):
    service = get_object_or_404(BatteryService, pk=pk)
    return render(request, "battery_service_receipt.html", {"service": service})

@login_required
@admin_required
def battery_report(request):
    services = BatteryService.objects.all().order_by("-date_time")
    total_amount = BatteryService.objects.aggregate(total=Sum("service_fee"))["total"] or 0

    return render(request, "battery_service_report.html", {
        "services": services,
        "total_amount": total_amount,
    })
