from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.forms import AuthenticationForm 
from .models import CustomUser  
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):  
    class Meta:  
        model = CustomUser  
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']  

        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'required': True,
                    'pattern': r'^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$',  
                    'type': 'email', 
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre Completo',
                    'required': True,
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Apellido Completo',
                    'required': True,
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Número de Control',
                    'required': True,
                    'pattern': r'^[0-9]{5}tn[0-9]{3}',  
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Edad',
                    'required': True,
                    'pattern': r'^[0-9]{2}$',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Número Telefónico',
                    'required': True,
                    'pattern': r'^[0-9]{10}$',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Contraseña',
                    'required': True,
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirme su Contraseña',
                    'required': True,
                }
            ),
        }


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su correo',
            'required': True,
            'pattern': r'^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$',  
            'type': 'email', 
        })
    )
    
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su Contraseña',
            'required': True,
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("username")  # AuthenticationForm usa `username`
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)  # Django usa `username`
            if not user:
                self.add_error('email', "Usuario o contraseña incorrectos.")

        return cleaned_data

    pass
