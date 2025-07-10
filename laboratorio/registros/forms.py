from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha_inicio', 'fecha_fin', 'campo1', 'campo2', 'campo3']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'campo1': forms.NumberInput(attrs={'class': 'form-control'}),
            'campo2': forms.NumberInput(attrs={'class': 'form-control'}),
            'campo3': forms.NumberInput(attrs={'class': 'form-control'}),
        }
