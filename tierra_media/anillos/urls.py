# urls.py

# Importamos las clases de django para manejar URLs
from django.urls import path 
from . import views # Importamos nuestras vistas definidas en views.py

urlpatterns = [

    # Definimos la url base, que mapea a la vista index 
    path('', views.index, name='index'),
    
    # Url para la galería de imágenes, mapeada a la vista galeria
    path('galeria/', views.galeria, name='galeria'),

    # Url para página de personajes, mapeada a vista personajes
    path('personajes/', views.personajes, name='personajes'),

    # Url para lugares en la Tierra Media, mapeada a vista lugares
    path('lugares/', views.lugares, name='lugares'), 
    
    path('registro/', views.registro, name='registro'),
    
    path('login/', views.login, name='login'),

]