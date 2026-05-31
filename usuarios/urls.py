from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_usuario),
    path('cadastro/', views.cadastro_login), 

]