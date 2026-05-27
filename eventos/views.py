from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request, 'home.html'),   

def cadastrar_evento(request):
     return render(request, 'eventos/cadastrar-evento.html')


