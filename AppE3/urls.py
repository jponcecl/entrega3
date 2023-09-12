from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('producto/', producto),
    path('categoria/', categoria),
    path('codigobarra/', codigobarra),
    path('usuario/', usuario),
]
