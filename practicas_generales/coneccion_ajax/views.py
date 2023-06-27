from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Suscriptor
# Create your views here.

def coneccion_ajax(request):
    suscriptoress = list(Suscriptor.objects.values())
    suscriptores = Suscriptor.objects.all()
    if request.method == 'GET':
        return render(request, 'index.html',{
            'suscriptores':suscriptores
    })  
    elif request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest': 
        suscriptor = Suscriptor.objects.create(nombre = request.POST['nombre'], email = request.POST['email'])
        suscriptor.save()
        suscriptoress = list(Suscriptor.objects.values())

        return JsonResponse({
            'sub':suscriptoress
        })
 
