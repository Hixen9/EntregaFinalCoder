from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UserEditForm(UserChangeForm):
    password = forms.CharField(help_text="",widget=forms.HiddenInput(),required=False)
    first_name = forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']
    def clean_password2(self):
        print(self.cleaned_data)
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("tus contraseñas no coinciden")
        return password2
    
class editBlog(forms.Form):
    tituloBlog = forms.CharField()
    textoBlog = forms.CharField()
    imagen = forms.ImageField()
