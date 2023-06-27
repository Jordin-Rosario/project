from django.urls import path
from . import views

urlpatterns = [
    path('coneccion/', views.coneccion_ajax, name = 'coneccion-ajax'),
]
