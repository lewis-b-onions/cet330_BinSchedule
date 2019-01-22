# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'firstname', 'lastname', 'mobile', 'postcode', 'door_number')
        help_texts = {
            'username': None,
            'password': None,
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'firstname', 'lastname', 'mobile', 'postcode', 'door_number')
        help_texts = {
            'username': None,
            'password': None,
        }
