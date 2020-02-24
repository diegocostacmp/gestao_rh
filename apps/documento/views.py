from .models import Documento
from django.views.generic import CreateView


class DocumentCreate(CreateView):
    model = Documento
    fields = ["descricao", "arquivo"]
