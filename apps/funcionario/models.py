from django.db import models
from django.contrib.auth.models import User

from apps.departamento.models import Departamento
from apps.empresa.models import Empresa

from django.urls import reverse

""" O termo "multitenancy de software" refere-se a uma arquitetura de 
software na qual uma única instância de software é executada em um 
servidor e atende a vários inquilinos. Sistemas projetados dessa 
maneira são freqüentemente chamados de compartilhados. """

class Funcionario(models.Model):
    nome            = models.CharField(max_length=100)
    user            = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento    = models.ManyToManyField(Departamento, default=None)
    empresa         = models.ForeignKey(Empresa, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_funcionario')
