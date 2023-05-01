from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tituloBlog = models.CharField( max_length=50)
    textoBlog = models.CharField( max_length=50)
    imagen = models.ImageField(upload_to='ImagenesBlogs/')


