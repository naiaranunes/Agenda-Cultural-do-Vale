from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento


@login_required
def criar_evento(request):

    if request.method == 'POST':

        Evento.objects.create(
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            local=request.POST.get('local'),
            data=request.POST.get('data'),
            categoria=request.POST.get('categoria'),
            imagem=request.FILES.get('imagem'),
            usuario=request.user
        )

        return redirect('meus_eventos')

    return render(request, 'eventos/criar_evento.html')


@login_required
def meus_eventos(request):

    eventos = Evento.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        'eventos/meus_eventos.html',
        {'eventos': eventos}
    )


@login_required
def editar_evento(request, id):

    evento = Evento.objects.get(id=id)

    # impede que um usuário edite evento de outro
    if evento.usuario != request.user:
        return redirect('meus_eventos')

    if request.method == 'POST':

        evento.titulo = request.POST.get('titulo')
        evento.descricao = request.POST.get('descricao')
        evento.local = request.POST.get('local')
        evento.data = request.POST.get('data')
        evento.categoria = request.POST.get('categoria')

        if request.FILES.get('imagem'):
            evento.imagem = request.FILES.get('imagem')

        evento.save()

        return redirect('meus_eventos')

    return render(
        request,
        'eventos/editar_evento.html',
        {'evento': evento}
    )


@login_required
def excluir_evento(request, id):

    evento = Evento.objects.get(id=id)

    # impede que um usuário exclua evento de outro
    if evento.usuario != request.user:
        return redirect('meus_eventos')

    evento.delete()

    return redirect('meus_eventos')
