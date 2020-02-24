from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.core import views
from apps.funcionario.api.views import FuncionarioViewSet
from apps.hora_extra.api.views import HoraExtraViewSet

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"api/funcionarios", FuncionarioViewSet)
router.register(r"api/hora_extra", FuncionarioViewSet)

urlpatterns = [
    path("", include("apps.core.urls")),
    path("funcionario/", include("apps.funcionario.urls")),
    path("departamento/", include("apps.departamento.urls")),
    path("empresa/", include("apps.empresa.urls")),
    path("document/", include("apps.documento.urls")),
    path("horas-extras/", include("apps.hora_extra.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
