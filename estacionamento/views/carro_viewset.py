# views.py
from rest_framework import viewsets

from ..models.carro import Carro
from ..serializers.carro_serializer import CarroSerializer


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
