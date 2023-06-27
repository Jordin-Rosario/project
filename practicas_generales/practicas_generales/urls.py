from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coneccion_ajax.urls')),
    path('', include('pruebaajax.urls')),
]
