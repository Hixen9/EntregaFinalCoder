from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("registrar/",register,name ="Register"),
    path('about/',About,name='About'),
]
