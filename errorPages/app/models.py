from django.db import models

class ErrorLog(models.Model):
    # Es igual a poner en varchar(10)
    codigo = models.CharField(max_length=10)
    # Es igual a longText
    mensaje = models.TextField()
    # Es igual a Date(now())
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{codigo} - {mensaje}"


