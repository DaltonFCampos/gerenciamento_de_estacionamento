# serializers.py
from datetime import datetime

from rest_framework import serializers

from ..models.reserva import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'carro', 'vaga', 'data_entrada', 'data_saida', 'valor']
        read_only_fields = ['data_entrada', 'data_saida', 'valor']

    def create(self, validated_data):
        validated_data['data_entrada'] = datetime.now()

        vaga = validated_data['vaga']
        vaga.disponivel = False
        vaga.save()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)