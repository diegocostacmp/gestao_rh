from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework import viewsets

from apps.core.serializers import GroupSerializer, UserSerializer
from apps.funcionario.models import Funcionario


@login_required
def home(request):
    data = {}
    data["usuario"] = request.user
    return render(request, "core/index.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
