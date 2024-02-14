from django.db import models


class Carro(models.Model):
    placa = models.CharField(
        max_length=20,
        unique=True,
    )

    modelo = models.CharField(
        max_length=100,
    )
    
    cor = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f"{self.placa} - {self.modelo} - {self.cor}"
