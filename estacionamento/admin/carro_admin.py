# admin.py
from django.contrib import admin

from ..models.carro import Carro


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'cor')
    search_fields = ('placa', 'modelo', 'cor')
