from django.urls import path, include
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraEditBase,
    HoraExtraDelete,
    HoraExtraCreate,
    UtilizouHoraExtra,
)

urlpatterns = [
    path("", HoraExtraList.as_view(), name="list_hora_extra"),
    path("novo/", HoraExtraCreate.as_view(), name="create_hora_extra"),
    path(
        "editar_funcionario/<int:pk>/",
        HoraExtraEdit.as_view(),
        name="update_hora_extra",
    ),
    path(
        "editar/<int:pk>/", HoraExtraEditBase.as_view(), name="update_hora_extra_base"
    ),
    path("deletar/<int:pk>/", HoraExtraDelete.as_view(), name="delete_hora_extra"),
    path(
        "utilizou-hora-extra/<int:pk>/",
        UtilizouHoraExtra.as_view(),
        name="utilizou_hora_extra",
    ),
]
