from .models import Alumnos
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import alumnoForm
from django.shortcuts import render

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]
    # http_method_names = ['GET', 'POST']

def agregar_alumno (request):
    form = alumnoForm()
    return render(request, 'agregarAlumnos.html', {'form': form})