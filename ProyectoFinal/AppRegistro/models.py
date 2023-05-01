from django.db import models

# Create your models here.
class Usuarios(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
 



