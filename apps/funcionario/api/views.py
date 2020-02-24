from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.funcionario.api.serializers import FuncionarioSerializer
from apps.hora_extra.api.serializers import HoraExtraSerializer
from apps.funcionario.models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    horaextra_set = HoraExtraSerializer(many=True)
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
