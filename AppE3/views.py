from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Categoria, CodigoBarra, Usuario

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")

def producto(req):
    return render(req, "producto.html")

def categoria(req):
    return render(req, "categoria.html")

def codigobarra(req):
    return render(req, "codigobarra.html")

def usuario(req):
    return render(req, "usuario.html")