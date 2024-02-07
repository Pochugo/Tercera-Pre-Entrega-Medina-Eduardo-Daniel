from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cliente', cliente, name="cliente"),
    path('comic', comic, name="comic"),
    path('distribuidor', distribuidor, name="distribuidor"),
    
    #RUTAS DE FORM
    
    path('clienteForm', clienteForm, name="clienteForm"),
    path('comicForm', comicForm, name="comicForm"),
    path('distribuidorForm', distribuidorForm, name="distribuidorForm"),
    
    path('buscar/', buscar, name="buscar"),
    path('buscarComic/', buscarComic, name="buscarComic"),
    
    
]