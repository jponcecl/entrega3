from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
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



def productoForm(req):
    if req.method == 'POST':
        prod = Producto(nombre=req.POST["nombre"],precio=req.POST["precio"])
        prod.save()
        return render(req, "busquedaProducto.html")
    else:
        return render(req, "productoForm.html")

def categoriaForm(req):
    if req.method == 'POST':
        cate = Categoria(nombre=req.POST["nombre"])
        cate.save()
        return render(req, "busquedaProducto.html")
    else:
        return render(req, "categoriaForm.html")

def codigobarraForm(req):
    if req.method == 'POST':
        codb = CodigoBarra(codigo=req.POST["codigo"])
        codb.save()
        return render(req, "busquedaProducto.html")
    else:
        return render(req, "codigobarraForm.html")

def usuarioForm(req):
    if req.method == 'POST':
        usu = Usuario(usuario=req.POST["usuario"],clave=req.POST["clave"],nombre=req.POST["nombre"],apat=req.POST["apat"],amat=req.POST["amat"],correo=req.POST["correo"])
        usu.save()
        return render(req, "busquedaProducto.html")
    else:
        return render(req, "usuarioForm.html")        

def busquedaProducto(req):
    return render(req, "busquedaProducto.html")

def buscarprod(req: HttpRequest):
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        prods  = Producto.objects.filter(nombre__icontains=nombre)
        return render(req, "resultadosBusquedaProducto.html", {"producto": prods})
    else:
        return HttpResponse(f"Debe ingresar un texto para buscar")