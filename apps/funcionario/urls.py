from django.urls import path, include
from .views import (
    FuncionarioList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioCreate,
    Pdf,
)

urlpatterns = [
    path("", FuncionarioList.as_view(), name="list_funcionario"),
    path("novo/", FuncionarioCreate.as_view(), name="create_funcionario"),
    path("editar/<int:pk>/", FuncionarioEdit.as_view(), name="update_funcionario"),
    path("deletar/<int:pk>/", FuncionarioDelete.as_view(), name="delete_funcionario"),
    path(
        "relatorio_funcionarios_html", Pdf.as_view(), name="relatorio_funcionarios_html"
    ),
]
