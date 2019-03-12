from django.urls import path
from .views import DocumentCreate

urlpatterns = [
    path('novo', DocumentCreate.as_view(), name='create_documento'),
    # path('editar/<int:pk>', EmpresaEdit.as_view(), name='edit_empresa'),
]
