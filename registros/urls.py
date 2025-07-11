from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('panel/', views.panel, name='panel'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
