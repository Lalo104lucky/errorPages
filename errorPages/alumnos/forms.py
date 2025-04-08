from django import forms
from .models import Alumnos

class alumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        widgets= {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre completo',
                    'required': True
                }
            ),
            'apellido': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                    'required': True
                }
            ),
            'edad': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True
                }
            ),
            'matricula': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Matricula',
                    'required': True
                }
            ),
            'correo': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Correo del alumno',
                    'required': True
                }
            )
        }

        labels = {
            'nombre': 'Nombre completo',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'matricula': 'Matricula',
            'correo': 'Correo'
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio',
            },
            'apellido': {
                'required': 'El apellido es obligatorio',
            },
            'edad': {
                'required': 'La edad es obligatoria',
                'invalid': 'Ingrese un número válido'
            },
            'matricula': {
                'required': 'La matricula es obligatoria',
            },
            'correo': {
                'required': 'El correo es obligatorio',
            }
        }