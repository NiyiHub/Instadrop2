from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Instadrop-home'), 
	path('shipment1/', views.shpmt_details_on_desk, name='Shipment-from-desk'), 
	path('details1/', views.sender_info, name='sender-info'), 
	path('details2/', views.receiver_info, name='receiver-info'),
	path('shipment2/', views.shpmt_details_from_home, name='Shipment-from-home'),
	path('shipped/', views.shipped_parcels, name='Shipped-parcels'), 
	path('track/', views.track_parcel, name='track-parcel'), 
	path('payment/', views.payment, name='make-payment'),
	path('about/', views.about, name='Instadrop-about'), 
]