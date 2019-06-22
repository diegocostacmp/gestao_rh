from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
    )
from .models import HoraExtra    

class HoraExtraList(ListView):
    model = HoraExtra

    # lista apenas os usuarios daquela empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = HoraExtra
    fields = ['motivo', 'funcionario', 'horas']   

class HoraExtraDelete(DeleteView):
    model = HoraExtra
    success_url =  reverse_lazy('list_hora_extra')
