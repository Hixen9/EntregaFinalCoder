from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    password1 = forms.CharField(label ='contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'repetir contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields}

