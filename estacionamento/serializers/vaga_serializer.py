from rest_framework import serializers

from ..models.vagas import Vaga


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['id', 'numero', 'tipo', 'disponivel']
