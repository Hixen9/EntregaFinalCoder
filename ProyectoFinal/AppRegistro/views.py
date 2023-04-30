from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registrarUsuario(request):

        return HttpResponse(f'No enviaste info')

def Home(request):
     return render(request,'Home.html')
