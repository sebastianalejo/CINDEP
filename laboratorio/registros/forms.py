from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'fecha_inicio', 'fecha_fin',
            'control1_promedio', 'control1_desviacion',
            'control2_promedio', 'control2_desviacion',
            'control3_promedio', 'control3_desviacion'
        ]
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'control1_promedio': forms.NumberInput(attrs={'class': 'form-control'}),
            'control1_desviacion': forms.NumberInput(attrs={'class': 'form-control'}),

            'control2_promedio': forms.NumberInput(attrs={'class': 'form-control'}),
            'control2_desviacion': forms.NumberInput(attrs={'class': 'form-control'}),

            'control3_promedio': forms.NumberInput(attrs={'class': 'form-control'}),
            'control3_desviacion': forms.NumberInput(attrs={'class': 'form-control'}),
        }
