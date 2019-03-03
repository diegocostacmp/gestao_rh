from django.urls import path, include
from .views import FuncionarioList, FuncionarioEdit, FuncionarioDelete

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionario'),
    path('editar/<int:pk>/', FuncionarioList.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioList.as_view(), name='delete_funcionario'),
    
]
