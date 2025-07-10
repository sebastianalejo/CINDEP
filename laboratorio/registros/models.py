from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    campo1 = models.IntegerField()
    campo2 = models.IntegerField()
    campo3 = models.IntegerField()

    def __str__(self):
        return f"Registro de {self.usuario.username}"

