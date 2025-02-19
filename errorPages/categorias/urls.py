from django.urls import path
from .views import *

urlpatterns = [
    path('ver/', getsCategoria, name='ver'),
    path('registrar/', registrarCategoria, name='registrar'),
    path('api/get/', jsonCategoria, name='lista'),
    path('json/', json1_view, name='json'),
]