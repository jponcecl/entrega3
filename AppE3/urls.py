from django.urls import path
from .views import *

urlpatterns = [
    path('', busquedaProducto, name="busquedaProducto"),
    path('producto/', producto, name="producto"),
    path('categoria/', categoria, name="categoria"),
    path('codigobarra/', codigobarra, name="codigobarra"),
    path('usuario/', usuario, name="usuario"),
    
    path('producto-form/', productoForm, name="productoForm"),
    path('categoria-form/', categoriaForm, name="categoriaForm"),
    path('codigobarra-form/', codigobarraForm, name="codigobarraForm"),
    path('usuario-form/', usuarioForm, name="usuarioForm"),
    
    path('busqueda-producto/', busquedaProducto, name="busquedaProducto"),
    path('buscar-prod/', buscarprod, name="buscarProd"),
]
