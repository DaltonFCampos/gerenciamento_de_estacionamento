# admin.py
from django.contrib import admin
from ..models.reserva import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('carro', 'vaga', 'data_entrada', 'data_saida', 'valor')
    search_fields = ('carro__placa', 'vaga__numero')
