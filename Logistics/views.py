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
            messages.success(request, f'Shipment has been created successfully!')
            return redirect('Instadrop-home')
    else:
        form = ParcelForm()
    return render(request, 'Logistics/shpmt_details_on_desk.html', {'form':form}) 


def sender_info(request):
    if request.method == 'POST':
        form = AddressDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receiver-info')
    else:
        form = AddressDetailsForm()
    return render(request, 'Logistics/sender_info.html', {'form':form})


def receiver_info(request):
    if request.method == 'POST':
        form = AddressDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Shipment-from-home')
    else:
        form = AddressDetailsForm()
    return render(request, 'Logistics/receiver_info.html', {'form':form})


def shpmt_details_from_home(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if Parcel.payment_type == 'Transfer' and form.is_valid():
            form.save()
            messages.success(request, f'Shipment has been created successfully!')
            return redirect('payment')

        else:
            form.save()
            messages.success(request, f'Shipment has been created successfully!')
            return redirect('Instadrop-home')
    else:
        form = ShipmentForm()
    return render(request, 'Logistics/shpmt_details_from_home.html', {'form':form}) 


def shipped_parcels(request):
    parcels = Parcel.objects.all()
    return render(request, 'Logistics/shipped_parcels.html', {'parcels': parcels})


def track_parcel(request):
    if request.method == 'POST':
        tracker = request.POST['tracker']
        parcels = Parcel.objects.filter(tracking_number__contains=tracker)

        return render(request, 'Logistics/track_parcel.html', {'tracker':tracker, 'parcels':parcels})
    else:
        return render(request, 'Logistics/track_parcel.html', {})


def payment(request):
    return render(request, 'Logistics/payment.html')    


def about(request):
    return render(request, 'Logistics/about.html')
