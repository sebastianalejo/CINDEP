from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro
from django.contrib.auth.decorators import login_required

@login_required
def formulario(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('dashboard')
    return render(request, 'formulario.html', {'form': form})

@login_required
def dashboard(request):
    registros = Registro.objects.filter(usuario=request.user)
    return render(request, 'dashboard.html', {'registros': registros})
