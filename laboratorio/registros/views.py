from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.http import HttpResponse
from django.utils.timezone import make_naive
import datetime

@login_required
def panel(request):
    form = RegistroForm()

    # 👤 Si es superusuario, ve todos los registros
    if request.user.is_superuser:
        registros = Registro.objects.all()
    else:
        registros = Registro.objects.filter(usuario=request.user)

    # 📝 Si se envió el formulario
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('panel')

    return render(request, 'panel.html', {'form': form, 'registros': registros})

@login_required
def exportar_excel(request):
    if request.user.is_superuser:
        registros = Registro.objects.all().values(
            'usuario__username',
            'fecha_envio',
            'fecha_inicio',
            'fecha_fin',
            'control1_promedio',
            'control1_desviacion',
            'control2_promedio',
            'control2_desviacion',
            'control3_promedio',
            'control3_desviacion'
        )
    else:
        registros = Registro.objects.filter(usuario=request.user).values(
            'fecha_envio',
            'fecha_inicio',
            'fecha_fin',
            'control1_promedio',
            'control1_desviacion',
            'control2_promedio',
            'control2_desviacion',
            'control3_promedio',
            'control3_desviacion'
        )

    df = pd.DataFrame(registros)

    # Convertir solo si es datetime con tz
    for col in ['fecha_envio', 'fecha_inicio', 'fecha_fin']:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: make_naive(x) if isinstance(x, datetime.datetime) and x.tzinfo else x
            )

    if request.user.is_superuser and 'usuario__username' in df.columns:
        df.rename(columns={'usuario__username': 'Laboratorio'}, inplace=True)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=registros.xlsx'
    df.to_excel(response, index=False, engine='openpyxl')
    return response