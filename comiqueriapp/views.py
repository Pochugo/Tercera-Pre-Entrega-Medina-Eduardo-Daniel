from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "comiqueriapp/home.html")

def cliente(request):
    contexto = {'cliente': Cliente.objects.all()}
    return render(request, "comiqueriapp/cliente.html", contexto)

def comic(request):
    contexto = {'comic': Comic.objects.all()}
    return render(request, "comiqueriapp/comic.html", contexto)

def distribuidor(request):
    contexto = {'distribuidor': Distribuidor.objects.all()}
    return render(request, "comiqueriapp/distribuidor.html", contexto)

# FORMS

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_telefono = miForm.cleaned_data.get("telefono")
            cliente = Cliente(apellido=cliente_apellido, nombre=cliente_nombre, telefono=cliente_telefono)
            cliente.save()
            return render(request, "comiqueriapp/clienteForm.html")
    else:
        miForm = ClienteForm()
       
    return render(request, "comiqueriapp/clienteForm.html", {"form": miForm})

def comicForm(request):
    if request.method == "POST":
        miForm = ComicForm(request.POST)
        if miForm.is_valid():
            comic_nombre = miForm.cleaned_data.get("nombre")
            comic_editoria = miForm.cleaned_data.get("editorial")
            comic_autor = miForm.cleaned_data.get("autor")
            comic = Comic(nombre=comic_nombre, editorial=comic_editoria, autor=comic_autor)
            comic.save()
            return render(request, "comiqueriapp/comicForm.html")
    else:
        miForm = ComicForm()
       
    return render(request, "comiqueriapp/comicForm.html", {"form": miForm})

def distribuidorForm(request):
    if request.method == "POST":
        miForm = DistribuidorForm(request.POST)
        if miForm.is_valid():
            distribuidor_nombre = miForm.cleaned_data.get("nombre")
            distribuidor_direccion = miForm.cleaned_data.get("direccion")
            distribuidor_telefono = miForm.cleaned_data.get("telefono")
            distribuidor = Distribuidor(nombre=distribuidor_nombre, direccion=distribuidor_direccion, telefono=distribuidor_telefono)
            distribuidor.save()
            return render(request, "comiqueriapp/distribuidorForm.html")
    else:
        miForm = DistribuidorForm()
       
    return render(request, "comiqueriapp/distribuidorForm.html", {"form": miForm})

# BUSCAR

def buscar(request):
    return render(request, "comiqueriapp/buscar.html")

def buscarComic(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        comic = Comic.objects.filter(nombre__icontains=patron)
        contexto = {"comic": comic}
        return render(request, "comiqueriapp/comic.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")