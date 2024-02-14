from django.db import models


class Vaga(models.Model):
    TIPO_CHOICES = [
        ("PADRAO", "Padrão"),
        ("DEFICIENTE", "Para Deficientes"),
        ("IDOSO", "Para Idosos"),
    ]

    numero = models.CharField(
        max_length=20,
        unique=True,
    )

    tipo = models.CharField(
        max_length=20, choices=TIPO_CHOICES, default="PADRAO"
    )

    disponivel = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"Vaga {self.numero} ({self.get_tipo_display()})"
