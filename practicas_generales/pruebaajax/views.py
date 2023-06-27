from django.shortcuts import render
from .models import AgregarMateria
from  django.http.response import JsonResponse

# Create your views here.
def buscar_materia(request):
    materias = AgregarMateria.objects.all()
    if request.method == 'GET':
        return render(request, 'asd.html', {
            'materias':materias
        })
    
    if request.method == 'POST':
        if 'creditos' in request.POST:
            add_materia = AgregarMateria.objects.create(materia = request.POST['nombre-materia'], creditos = request.POST['creditos'])
            add_materia.save()
            return render(request, 'asd.html', {
            'materias':materias
        })
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            materia = list(AgregarMateria.objects.filter(materia = request.POST['nombre-materia']).values())
            
            return JsonResponse({
                "materia":materia,
            })
             