from django.contrib import admin
from .models import Producto, Categoria, CodigoBarra, Usuario

# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(CodigoBarra)
admin.site.register(Usuario)