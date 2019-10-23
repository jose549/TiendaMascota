from django.shortcuts import render
from mascotas.models import Producto

# Create your views here.

def index(request):
    lista_productos = Producto.objects.all()
    
    return render(request, 'index.html', {'lista_prod' : lista_productos})

def indexPerro(request):
    return render(request, 'indexPerro.html')

def indexGato(request):
    return render(request, 'indexGato.html')

def indexCuy(request):
    return render(request, 'indexCuy.html')

def crearCuenta(request):
    return render(request, 'formularioCuenta.html')

def contacto(request):
    return render(request, 'formularioContacto.html')