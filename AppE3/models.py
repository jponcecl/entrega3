from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} - {self.precio}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.nombre}'

class CodigoBarra(models.Model):
    codigo = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.codigo}'

class Usuario(models.Model):
    usuario = models.CharField(max_length=32)
    clave = models.CharField(max_length=32)
    nombre = models.CharField(max_length=32)
    apat = models.CharField(max_length=20)
    amat = models.CharField(max_length=20)
    correo = models.EmailField()
    def __str__(self):
        return f'{self.usuario} - {self.clave} - {self.nombre} - {self.apat} - {self.amat} - {self.correo}'
    
# 1) En "settings.py" agregar APP, en este caso 'AppE3' a INSTALLED_APPS
# 2) python3 manage.py showmigrations
# 3) python3 manage.py makemigrations
# 4) python3 manage.py migrate
