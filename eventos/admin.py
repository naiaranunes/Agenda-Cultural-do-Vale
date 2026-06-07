from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'categoria',
        'local',
        'usuario',
        'data'
    )

    search_fields = (
        'titulo',
        'local'
    )

    list_filter = (
        'categoria',
        'data'
    )