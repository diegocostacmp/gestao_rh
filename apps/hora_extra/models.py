from django.db import models
from apps.funcionario.models import Funcionario


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.motivo
