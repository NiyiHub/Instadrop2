from django.shortcuts import render

def home(request):
    return render(request, 'Logistics/index.html')


def about(request):
    return render(request, 'Logistics/about.html')
