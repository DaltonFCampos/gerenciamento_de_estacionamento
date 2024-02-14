from django.contrib import admin

from ..models.vagas import Vaga


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'disponivel')
    search_fields = ('numero',)
    list_filter = ('tipo', 'disponivel')
