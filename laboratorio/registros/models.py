from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    
    control1_promedio = models.FloatField(null=True, blank=True)
    control1_desviacion = models.FloatField(null=True, blank=True)
    
    control2_promedio = models.FloatField(null=True, blank=True)
    control2_desviacion = models.FloatField(null=True, blank=True)
    
    control3_promedio = models.FloatField(null=True, blank=True)
    control3_desviacion = models.FloatField(null=True, blank=True)
    
    fecha_envio = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return f"Registro de {self.usuario.username}"
