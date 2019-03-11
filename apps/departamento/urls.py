from django.urls import path
from .views import (
    DepartamentoList
)

urlpatterns = [
    path('list', DepartamentoList.as_view(), name='list_departamento'),
    # path('', FuncionarioList.as_view(), name='list_funcionario'),
    # path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    # path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    # path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
