from django import forms
from .models import DailyBuy


class DailyBuyForm(forms.ModelForm):

    class Meta:
        model = DailyBuy
        fields = ('name', 'what_to_buy', 'description','where_to_buy', 'delivery_address', 'phone_number')
        
    labels = {
            'name': 'Name',
            'what_to_buy': 'Item',
            'description': 'Description',
            'where_to_buy': 'From',
            'delivery_address': 'Delivery Location',
            'phone_number': 'Phone Number'
        }


    widgets = {
            'name':                 forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full name'}),
            'what_to_buy':          forms.Select(attrs={'class':'form-select', 'placeholder': 'Item'}),
            'description':          forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description of item/list of items'}),
            'where_to_buy':         forms.Select(attrs={'class':'form-select', 'placeholder': 'From'}),
            'delivery_address':     forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Delivery address'}),
            'phone_number':         forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'})
        }   