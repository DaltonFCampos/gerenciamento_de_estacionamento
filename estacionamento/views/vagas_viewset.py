from rest_framework import viewsets

from ..models.vagas import Vaga
from ..serializers.vaga_serializer import VagaSerializer


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
