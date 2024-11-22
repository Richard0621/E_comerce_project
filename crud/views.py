from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Productos
# Create your views here.
def index(request):
    lista_productos = Productos.objects.all()
    template = loader.get_template("index.html") 
    context = {'productos': lista_productos}
    return HttpResponse(template.render(context,request))

def detalles(request, producto_id):
    detalles_producto = Productos.objects.get(id=producto_id)
    template = loader.get_template("detail.html")
    context = {'productos': detalles_producto}
    return HttpResponse(template.render(context,request))