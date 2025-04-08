from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnosViewSet
from .views import agregar_alumno

router = SimpleRouter()
router.register(r'api', AlumnosViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar_alumno, name='agregar_alumno')
]