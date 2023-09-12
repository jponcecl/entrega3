from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('producto/', producto, name="producto"),
    path('categoria/', categoria, name="categoria"),
    path('codigobarra/', codigobarra, name="codigobarra"),
    path('usuario/', usuario, name="usuario"),
]
