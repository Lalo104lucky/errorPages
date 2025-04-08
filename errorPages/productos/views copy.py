from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse

# Agregar un producto

def agregarProducto(request):
    # Primero checamos como llegamos a esta funcion
    if request.method == 'POST':
        # LLegamos aqui por el envío de un formulario
        form = productoForm(request.POST) # Genera un formulario lleno con información
        if form.is_valid():
            form.save()
            return redirect('ver') # Esto redirige a la vista del producto
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form':form})

# Ver los productos
def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ver.html', {'productos':productos})

# Devuelve el JSON
def lista_productos(request):
    productos = Producto.objects.all()
    # Para enviar un JSON debemos escribir los datos en un diccionario usando llaves
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen,
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)

def json_view(request):
    return render(request, 'json.html')

import json
# @CSRF_exempt <---- No es seguro hacer esto (no lo hagas)

def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen'] 
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nuevo_producto.id
            },status=201
            )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)
    return JsonResponse({
        'error': 'Método no es POST'
    }, status = 405)
