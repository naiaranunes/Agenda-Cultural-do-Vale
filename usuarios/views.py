from django.shortcuts import render
# Create your views here.
#cadastro de usuários
def cadastro_login(request):
    return render(request, 'usuarios/cadastro-usuario.html')

def login_usuario(request):
    return render(request, 'usuarios/login.html')

from django.shortcuts import redirect

def logout_usuario(request):
    try:
        del request.session["usuario_id"]
    except KeyError:
        pass

    return redirect('/')
