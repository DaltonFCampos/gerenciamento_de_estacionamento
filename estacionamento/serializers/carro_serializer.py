# serializers.py
from rest_framework import serializers

from ..models.carro import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'placa', 'modelo', 'cor']
