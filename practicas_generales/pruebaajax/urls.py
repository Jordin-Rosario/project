from django.urls import path
from . import views

urlpatterns = [
    path('buscar/', views.buscar_materia, name = 'buscar-materia')
]
