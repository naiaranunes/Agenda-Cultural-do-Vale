from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cadastrar_evento(request):
     return render(request, 'eventos/cadastrar-evento.html')


def listar_eventos(request):
     return render(request, 'eventos/listar-evento.html')

