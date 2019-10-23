from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.index, name = 'index'),
    path('home/perro/', views.indexPerro, name = 'indexPerro'),
    path('home/gato/', views.indexGato, name = 'indexGato'),
    path('home/cuy/', views.indexCuy, name = 'indexCuy'),
    path('home/crearCuenta/', views.crearCuenta, name = 'crearCuenta'),
    path('home/contacto/', views.contacto, name = 'contacto'),
]