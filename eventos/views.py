from django.shortcuts import redirect, render
from .forms import EventoForm
def home(request):
    return render(request, 'home.html')

def cadastrar_evento(request):

    if request.method == 'POST':
        print("CHEGOU NO POST")

        form = EventoForm(request.POST, request.FILES)

        if form.is_valid():
            print("FORMULÁRIO VÁLIDO")
            form.save()
            return redirect('listar_eventos')
        else:
            print(form.errors)

    else:
        form = EventoForm()

    return render(
        request,
        'eventos/cadastrar-evento.html',
        {'form': form}
    )

def listar_eventos(request):
     return render(request, 'eventos/listar-evento.html')

