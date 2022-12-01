from django.db import models
from django.contrib.auth.models import User

#create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)#fecha de cuando se crea el objeto.
    foto = models.ImageField(null=True, blank=True)

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete= models.CASCADE)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    contenido = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

#sistema de "me gusta"