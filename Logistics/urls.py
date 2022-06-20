from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Instadrop-home'), 
	path('shipment/', views.shpmt_details_on_desk, name='Shipment-from-desk'), 
	path('about/', views.about, name='Instadrop-about'), 
]