# Generated by Django 4.2.3 on 2024-02-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vaga",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.CharField(max_length=20, unique=True)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("PADRAO", "Padrão"),
                            ("DEFICIENTE", "Para Deficientes"),
                            ("IDOSO", "Para Idosos"),
                        ],
                        default="PADRAO",
                        max_length=20,
                    ),
                ),
                ("disponivel", models.BooleanField(default=True)),
            ],
        ),
    ]
