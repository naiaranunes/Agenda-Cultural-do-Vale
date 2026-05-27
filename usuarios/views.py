from django.shortcuts import render
# Create your views here.
def login_usuario(request):
    return render(request, 'usuarios/login.html')

