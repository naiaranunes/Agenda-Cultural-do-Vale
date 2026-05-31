from django.shortcuts import render
# Create your views here.
#cadastro de usuários
def cadastro_login(request):
    return render(request, 'usuarios/cadastro-usuario.html')

def login_usuario(request):
    return render(request, 'usuarios/login.html')

