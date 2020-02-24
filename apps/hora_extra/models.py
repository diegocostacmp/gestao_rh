from django.db import models
from django.urls import reverse
from apps.funcionario.models import Funcionario


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, default=None)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("update_funcionario", args=[self.funcionario.id])

    def __str__(self):
        return self.motivo
