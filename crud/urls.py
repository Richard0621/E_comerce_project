from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detalle/<producto_id>/', views.detalles, name='detalleProducto'),
]