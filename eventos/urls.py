from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar-evento/', views.cadastrar_evento, name='cadastrar_evento'),
]

