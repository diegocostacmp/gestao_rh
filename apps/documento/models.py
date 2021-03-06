from django.db import models
from apps.funcionario.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, null=True, blank=True, default=None
    )
    arquivo = models.FileField(upload_to="documentos")

    def __str__(self):
        return self.descricao
