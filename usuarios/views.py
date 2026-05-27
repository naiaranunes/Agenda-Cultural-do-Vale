from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def login_usuario(request):
    return HttpResponse('pagina de login')