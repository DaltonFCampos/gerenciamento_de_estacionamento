# views.py
from datetime import datetime, timedelta, timezone

import pytz
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.reserva import Reserva
from ..serializers.reserva_serializer import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    @action(detail=True, methods=["post"])
    def finalizar_reserva(self, request, pk=None):
        try:
            reserva = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response(
                {"error": "Reserva não encontrada."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if reserva.data_saida:
            return Response(
                {"error": "Esta reserva já foi finalizada."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # gambiarrra pra pegar o horário do Brasil
        data_saida = datetime.now(timezone.utc) - timedelta(hours=3)
        reserva.data_saida = data_saida

        tempo_de_reserva = data_saida - reserva.data_entrada
        horas_de_reserva = tempo_de_reserva.total_seconds() / 3600
        valor_por_hora = 10
        reserva.valor = horas_de_reserva * valor_por_hora

        reserva.vaga.disponivel = True
        reserva.vaga.save()

        reserva.save()

        serializer = self.get_serializer(reserva)
        return Response(serializer.data)
