"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/', views.registro1, name='registro_usuario'),
    path('logueo/,', views.login2, name='logueo'),
    path('logout/', views.logout2, name='logout'),
    path('listar/', views.Listar_Noticias, name='listar'),
    path('Detalle/<int:pk>', views.Detalle_Noticias, name='detalle'),
    path('Comentario/', views.Comentar_Noticia, name='comentar'),

]
