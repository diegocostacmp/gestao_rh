from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
    )
from .models import HoraExtra    
from .forms import HoraExtraForm

class HoraExtraList(ListView):
    model = HoraExtra

    # lista apenas os usuarios daquela empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm
    
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