from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Categoria, CodigoBarra, Usuario

# Create your views here.

def inicio(req):
    return HttpResponse("Vista inicio")

def producto(req):
    return HttpResponse("Vista producto")

def categoria(req):
    return HttpResponse("Vista categoria")

def codigobarra(req):
    return HttpResponse("Vista CodigoBarra")

def usuario(req):
    return HttpResponse("Vista usuario")