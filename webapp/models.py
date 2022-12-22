from django.db import models
from django.contrib.auth.models import User


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='static/img')
    categoria_noticia = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(max_length=1500)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{Comentario.noticia}->{Comentario.texto}'
