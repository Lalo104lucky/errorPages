from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse

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
