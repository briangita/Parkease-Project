from django.shortcuts import render, redirect, get_object_or_404
from .models import TyreService
from .forms import TyreServiceForm
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required


# Create your views here.
@login_required
def tyre_service_list(request):
    services = TyreService.objects.all().order_by('-date_time')
    return render(request, 'tyre_service_list.html', {'services': services})

@login_required
def tyre_service_form(request):
    if request.method == 'POST':
        form = TyreServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tyre_service_receipt', pk=form.instance.pk)
    else:
        form = TyreServiceForm()
    return render(request, 'tyre_service_form.html', {'form': form})
@login_required
def tyre_service_receipt(request, pk):
    service = get_object_or_404(TyreService, pk=pk)
    return render(request, 'tyre_service_receipt.html', {'service': service})

@login_required
@admin_required
def tyre_service_report(request):
    services = TyreService.objects.all().order_by('-date_time')
    total_revenue = sum(service.service_fee for service in services)
    return render(request, 'tyre_service_report.html', {'services': services, 'total_revenue': total_revenue})