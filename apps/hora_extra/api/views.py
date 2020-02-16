from rest_framework import viewsets
from apps.hora_extra.api.serializers import HoraExtraSerializer
from apps.hora_extra.models import HoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class HoraExtraViewSet(viewsets.ModelViewSet):
    queryset = HoraExtra.objects.all()
    serializer_class = HoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
