from django.urls import path
from . import views

urlpatterns = [

    path('novo/', views.criar_evento, name='criar_evento'),

    path('meus-eventos/',views.meus_eventos,name='meus_eventos'),

    path('editar/<int:id>/',views.editar_evento, name='editar_evento'),

    path('excluir/<int:id>/',views.excluir_evento,name='excluir_evento'),
    
    path('todos-eventos/', views.todos_eventos, name='todos_eventos'),
]

