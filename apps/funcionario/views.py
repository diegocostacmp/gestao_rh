from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
    )
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

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
