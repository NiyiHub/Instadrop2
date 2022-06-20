from django.shortcuts import render, redirect
from .forms import ParcelForm, AddressDetailsForm, ShipmentForm
from .models import Parcel
from django.contrib import messages


def home(request):
    return render(request, 'Logistics/index.html')


def shpmt_details_on_desk(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Shipment created successfully!')
            return redirect('Instadrop-home')
    else:
        form = ParcelForm()
    return render(request, 'Logistics/shpmt_details_on_desk.html', {'form':form}) 


def about(request):
    return render(request, 'Logistics/about.html')
