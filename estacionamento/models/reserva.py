from django.db import models

from .carro import Carro
from .vagas import Vaga


class Reserva(models.Model):
    carro = models.ForeignKey(
        Carro,
        on_delete=models.CASCADE,
    )

    vaga = models.ForeignKey(
        Vaga,
        on_delete=models.CASCADE,
    )

    data_entrada = models.DateTimeField()

    data_saida = models.DateTimeField(null=True)

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True
    )

    def __str__(self):
        return f"Reserva: Carro {self.carro} | Vaga {self.vaga} | Entrada: {self.data_entrada} - Saída: {self.data_saida} | Valor: R${self.valor}"
