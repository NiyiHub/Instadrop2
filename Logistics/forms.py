from django import forms
from .models import Parcel, AddressDetails

class ParcelForm(forms.ModelForm):
    
    class Meta:
        model = Parcel
        fields = ('delivery_date', 'parcel_content', 'parcel_weight',
                    'sender', 'sender_mobile', 'sender_address', 'receiver', 'receiver_mobile',
                    'receiver_address', 'shipping_agent')

        labels = {
            'delivery_date': 'Delivery date (YYYY-MM-DD)',
            'parcel_content': 'Parcel content',
            'parcel_weight': 'Parcel weight',
            'sender': "Sender's name",
            'sender_mobile': "Sender's phone number",
            'sender_address': "Sender's address",
            'receiver': "Receiver's name",
            'receiver_mobile': "Receiver's phone number",
            'receiver_address': "Receiver's address",
            'shipping_agent': 'shipping_agent'
        }


        widgets = {
            'delivery_date':        forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Delivery Date'}),
            'parcel_content':       forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Content'}),
            'parcel_weight':        forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Weight in KG'}),
            'sender':               forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sender'}),
            'sender_mobile':        forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sender Mobile'}),
            'sender_address':       forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sender Address'}),
            'receiver':             forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Receiver'}),
            'receiver_mobile':      forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Receiver Mobile'}),
            'receiver_address':     forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Reiceiver Address'}),
            'shipping_agent':       forms.Select(attrs={'class': 'form-select', 'placeholder': 'shipping_agent'})
        }


class ShipmentForm(forms.ModelForm):

    class Meta:
        model = Parcel
        fields = ('delivery_date', 'delivery_address', 'parcel_content', 'parcel_weight',
                    'shipment_note', 'pickup_date', 'parcel_type', 'payment_type', 'shipping_agent')

        labels = {
            'delivery_date': 'Delivery date (YYYY-MM-DD)',
            'delivery_address': 'Delivery address',
            'parcel_content': 'Parcel content',
            'parcel_weight': '',
            'shipment_note': 'Shipment note',
            'pickup_date': 'Pickup date (YYYY-MM-DD)',
            'parcel_type': 'Parcel type',
            'payment_type': 'Payment method',
            'shipping_agent': 'shipping_agent'
        }

        widgets = {
            'delivery_date':    forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Delivery Date'}),
            'delivery_address': forms.Select(attrs={'class':'form-select', 'placeholder': 'Delivery Address'}),
            'parcel_content':   forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Content'}),
            'parcel_weight':    forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Weight in KG'}),
            'shipment_note':    forms.Textarea(attrs={'class':'form-control', 'placeholder': '(Optional)'}),
            'pickup_date':      forms.DateInput(attrs={'class':'form-control', 'placeholder': 'PickUp Date'}),
            'parcel_type':      forms.Select(attrs={'class':'form-select', 'placeholder': 'Parcel Type'}),
            'payment_type':     forms.Select(attrs={'class':'form-select', 'placeholder': 'Payment Method'}),
            'shipping_agent':   forms.Select(attrs={'class': 'form-select', 'placeholder': 'shipping_agent'})
        }


class AddressDetailsForm(forms.ModelForm):
    
    class Meta:
        model = AddressDetails
        fields = ('name', 'company', 'email', 'address', 'city', 'state', 'mobile')

        labels = {
            'name': 'Full name',
            'company': 'Company/Brand name',
            'email': 'Email address',
            'address': 'Address',
            'city': 'City/province',
            'state': 'State',
            'mobile': 'Phone number'
        }
        
        widgets = {
            'name':     forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
            'company':  forms.TextInput(attrs={'class':'form-control', 'placeholder': '(Optional)'}),
            'email':    forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}),
            'address':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'city':     forms.TextInput(attrs={'class':'form-control', 'placeholder': 'City/Province'}),
            'state':    forms.TextInput(attrs={'class':'form-control', 'placeholder': 'State'}),
            'mobile':   forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Mobile'}),
        }

