from rest_framework import serializers
from apps.funcionario.models import Funcionario
from apps.hora_extra.api.serializers import HoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    horaextra_set = HoraExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = (
            'id', 'nome', 'departamentos', 
            'empresa', 'user', 'imagem',
            'total_horas_extra', 'horaextra_set')
