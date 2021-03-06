from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserAccount, Profile
from django.conf import settings
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = UserAccount
        fields = ('email', 'full_name', 'phone', 'address', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login details. Try again!')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserAccount
        fields = ['email', 'phone', 'phone2', 'address']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'brand_name', 'about_brand']