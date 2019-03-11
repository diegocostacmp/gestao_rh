from django.urls import path
from .views import (
    DepartamentoList,
    DepartamentoCreate,
    DepartamentoUpdate,

)

urlpatterns = [
    path('list', DepartamentoList.as_view(), name='list_departamento'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>/', DepartamentoUpdate.as_view(), name='update_departamento'),
    # path('', FuncionarioList.as_view(), name='list_funcionario'),
    # path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
