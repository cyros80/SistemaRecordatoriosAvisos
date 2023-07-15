from django import forms
from .models import Pendientes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from dataclasses import fields

class PendientesForm(forms.ModelForm):
    class Meta:
        model=Pendientes
        fields=[
            'Area','tarea'
        ]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email', 'password1', 'password2','groups']        