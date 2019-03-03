from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Funcionario



class FuncionarioList(ListView):
    model = Funcionario

# lista apenas os usuarios daquela empresa
def get_queryset(self):
    empresa_logada = self.request.user.funcionario.empresa
    queryset = Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']    

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url =  reverse_lazy('list_funcionario')
