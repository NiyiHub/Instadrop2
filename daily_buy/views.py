from django.shortcuts import render, redirect
from .models import DailyBuy
from .forms import DailyBuyForm
from django.contrib import messages


def place_order(request):
    if request.method == 'POST':
        form = DailyBuyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Order has been placed successfully!')
            return redirect('Instadrop-home')
    else:
        form = DailyBuyForm()
    return render(request, 'daily_buy/place_order.html', {'form':form})
