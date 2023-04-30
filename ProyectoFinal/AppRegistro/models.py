from django.db import models

# Create your models here.
class Usuarios(models.Model):
    IdUsuario = models.IntegerField()
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=50)

class Admin(models.Model):
    nombre = models.CharField( max_length=50)
    contraseña = models.CharField( max_length=50)
