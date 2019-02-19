from django.urls import path, include
from .views import FuncionarioList

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionario'),
    
]
