from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt 

def registrarCategoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = categoriaForm()
    return render(request, 'registrar.html', {'form':form})

def getsCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'gets.html', {'categorias':categorias})

def jsonCategoria(request):
    categorias = Categoria.objects.all()
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen,
        }
        for c in categorias
    ]

    return JsonResponse(data, safe=False)

def json1_view(request):
    return render(request, 'jsoncategoria.html')

import json
# @CSRF_exempt <---- No es seguro hacer esto (no lo hagas)

def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nueva_categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen'] 
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nueva_categoria.id
            },status=201
            )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)
    return JsonResponse({
        'error': 'Método no es POST'
    }, status = 405)
