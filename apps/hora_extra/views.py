from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
    )
from django.views import View
from .models import HoraExtra    
from .forms import HoraExtraForm
import json
from django.http import HttpResponse

class HoraExtraList(ListView):
    model = HoraExtra

    # lista apenas os usuarios daquela empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEditBase(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm
    # success_url = reverse_lazy('update_hora_extra_base')
    
    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    # Injeta os args necessarios para filtrar a listagem de
    #  usuarios por empresa no edit
    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraEdit(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('update_hora_extra_base')
    
    # Injeta os args necessarios para filtrar a listagem de
    #  usuarios por empresa no edit
    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraDelete(DeleteView):
    model = HoraExtra
    success_url =  reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = HoraExtra
    form_class = HoraExtraForm
    
    # Injeta os args necessarios para filtrar a listagem de
    #  usuarios por empresa no create
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        hora_extra = HoraExtra.objects.get(id=kwargs['pk'])
        hora_extra.utilizada = True
        hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'Requisicao executada',
                'horas': float(empregado.total_horas_extra)
            }
        )
        return HttpResponse(response, 
            content_type='application/json')

