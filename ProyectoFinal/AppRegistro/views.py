from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .views import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *


# Create your views here.
def register(request):
      if request.method == 'POST':
            miFormulario = UserRegisterForm(request.POST)

            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data
                  username = data["username"]
                  miFormulario.save()
                  return render(request,"Home.html",{"mensaje2":f"El usuario {username} ha sido Creado!"})
            else:
                  miFormulario = UserRegisterForm()
                  return render(request,"signup.html",{"mensaje1":"El Usuario no ha sido creado revisa si has ingresado los datos correctamente","miFormulario": miFormulario})
                  
      
      else:
            miFormulario = UserRegisterForm()    
            return render(request,"signup.html",{"miFormulario": miFormulario})



def Home(request):
     return render(request,'Home.html')

def About(request):
      return render(request,'About.html')
