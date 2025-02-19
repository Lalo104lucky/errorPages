from django import forms
from .models import Categoria

class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']

        widgets= {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la categoría',
                    'required': True
                }
            ),
            'imagen': forms.URLInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen de la categoría',
                    'required': True
                }
            )
        }

        labels = {
            'nombre': 'Nombre de la categoría',
            'imagen': 'URL de la imagen'
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio',
            }
        }