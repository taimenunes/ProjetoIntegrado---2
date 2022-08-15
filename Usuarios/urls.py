from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('agendar', views.agendar, name='agendar'),
    path('logout', views.logout, name='logout'),
    path('agendamentos', views.agendamentos, name='agendamentos')
]