from django.views.generic import ListView, CreateView, UpdateView
from .models import Departamento


# lista apenas os usuarios daquela empresa
class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']
