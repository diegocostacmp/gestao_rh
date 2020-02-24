from rest_framework import serializers
from apps.hora_extra.models import HoraExtra


class HoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraExtra
        fields = ("id", "motivo", "funcionario", "horas", "utilizada")
