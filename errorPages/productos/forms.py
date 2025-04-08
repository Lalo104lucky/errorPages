from django import forms
from .models import Producto

# Podemos crear un formulario para cada modelo que exista
class productoForm(forms.ModelForm):
    # La clase Meta (MetaInfo del formulario):
    class Meta:

        # Definir de que modelo se basa el formulario
        model = Producto

        # Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'precio', 'imagen', 'categoria']

        # Definir como se deben de ver o atributos tienen los campos
        widgets= {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                    'required': True
                }
            ),
            'precio': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Precio',
                    'required': True
                }
            ),
            'imagen': forms.URLInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen del producto',
                    'required': True
                }
            ),
            'categoria': forms.Select(
                attrs= {
                    'class': 'form-control',
                    'required': True
                }
            )
        }

        #Etiqutas personalizadas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }

        # Mensajes de error personalizados
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio',
            },
            'precio': {
                'required': 'El precio no puede estar vacío',
                'invalid': 'Ingrese un número válido'
            }
        }