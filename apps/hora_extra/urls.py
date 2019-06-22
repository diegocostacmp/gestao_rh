from django.urls import path, include
from .views import (
    HoraExtraList,
    HoraExtraEdit
    # FuncionarioDelete, 
    # FuncionarioCreate
    )

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    # path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    
]
