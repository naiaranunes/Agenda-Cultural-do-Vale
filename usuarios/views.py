from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from eventos.models import Evento


# Create your views here.

def home(request):
        eventos = Evento.objects.all()
        return render(request,'home.html',{'eventos': eventos})

def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')

    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('password')

    user = User.objects.filter(username=username).first()

    if user:
        messages.error(request, 'Já existe um usuário com esse nome.')
        return redirect('cadastro')

    user = User.objects.create_user(
        username=username,
        email=email,
        password=senha
    )

    user.save()

    messages.success(
        request,
        'Usuário cadastrado com sucesso!'
    )

    return redirect('login')

def login(request):
    if request.method == "GET":
        return(render(request, 'login.html'))
    else:
        username = request.POST.get('username')
        senha =  request.POST.get('senha')

        print("USERNAME:", username)
        print("SENHA:", senha)
        
        user = authenticate(username=username, password=senha)
        print(user)
        if user:
            login_django(request, user)
            return redirect('plataforma')
        else:
            return HttpResponse('email ou senha invalidos')
@login_required(login_url="/auth/login/")
def plataforma(request):
    return render(request, 'plataforma.html')



def sair(request):
    logout(request)
    return redirect('home')

def home(request):

    eventos = Evento.objects.all()

    return render(
        request,
        'home.html',
        {'eventos': eventos}
    )

