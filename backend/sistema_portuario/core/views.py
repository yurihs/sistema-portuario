from django.contrib.auth.models import Group
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from sistema_portuario.core import models, serializers


class PutOnlyModelMixin:
    def update(self, request, *args, **kwargs):
        return mixins.UpdateModelMixin.update(self, request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()


class ModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    PutOnlyModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class GrupoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GrupoSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class UsuarioViewSet(ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def retrieve(self, request, *args, **kwargs):
        if not request.user.has_perm("core.view_usuario"):
            raise PermissionDenied()
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not request.user.has_perm("core.view_usuario"):
            raise PermissionDenied()
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=["get"], url_path="atual")
    def get_current(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class EmpresaViewSet(ModelViewSet):
    queryset = models.Empresa.objects.select_related("endereco")
    serializer_class = serializers.EmpresaSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    @action(detail=True, methods=["get"], url_path="navios")
    @swagger_auto_schema(
        responses={200: serializers.EmpresaNaviosListSerializer(many=True)}
    )
    def get_navios(self, request, pk):
        instance = self.get_object()
        serializer = serializers.EmpresaNaviosListSerializer(
            instance=instance.navios.all(), many=True
        )
        return Response(serializer.data)


class TipoCargaViewSet(ModelViewSet):
    queryset = models.TipoCarga.objects.all()
    serializer_class = serializers.TipoCargaSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class NavioViewSet(ModelViewSet):
    queryset = models.Navio.objects.select_related(
        "empresa__endereco"
    ).prefetch_related("tipos_de_carga_suportados")
    serializer_class = serializers.NavioSerializer
    lookup_field = "numero_imo"
    permission_classes = [permissions.DjangoModelPermissions]

    @action(detail=True, methods=["get"], url_path="viagens")
    @swagger_auto_schema(
        responses={200: serializers.NavioViagensListSerializer(many=True)}
    )
    def get_viagens(self, request, numero_imo):
        instance = self.get_object()
        serializer = serializers.NavioViagensListSerializer(
            instance=instance.viagens.all(), many=True
        )
        return Response(serializer.data)


class PortoViewSet(ModelViewSet):
    queryset = models.Porto.objects.select_related("endereco")
    serializer_class = serializers.PortoSerializer
    lookup_field = "un_locode"
    permission_classes = [permissions.DjangoModelPermissions]

    @action(detail=True, methods=["get"], url_path="viagens")
    @swagger_auto_schema(
        responses={200: serializers.PortoViagensListSerializer(many=True)}
    )
    def get_viagens(self, request, un_locode):
        instance = self.get_object()
        serializer = serializers.PortoViagensListSerializer(
            instance=instance.viagens.all(), many=True
        )
        return Response(serializer.data)


class ViagemViewSet(ModelViewSet):
    queryset = models.Viagem.objects.select_related(
        "navio", "navio__empresa__endereco", "porto_origem__endereco"
    ).prefetch_related("navio__tipos_de_carga_suportados", "cargas")
    serializer_class = serializers.ViagemSerializer
    permission_classes = [permissions.DjangoModelPermissions]
