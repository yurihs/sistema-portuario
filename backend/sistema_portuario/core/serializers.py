from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from sistema_portuario.core import fields, models


class GrupoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(label="Nome", source="name")

    class Meta:
        model = Group
        fields = ["nome"]
        read_only_fields = ["nome"]


class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="ID", read_only=True)
    email = serializers.EmailField(
        label="E-mail",
        max_length=254,
        validators=[
            validators.UniqueValidator(
                queryset=models.Usuario.objects.all(),
                message="Já existe um usuário com este e-mail.",
            )
        ],
    )
    password = serializers.CharField(label="Senha", max_length=128, write_only=True)
    cpf = fields.CPFField(
        label="CPF",
        max_length=255,
        validators=[
            validators.UniqueValidator(
                queryset=models.Usuario.objects.all(),
                message="Já existe um usuário com este CPF.",
            )
        ],
    )
    grupo = fields.SingleGroupField(label="Grupo", source="groups")

    def validate_password(self, value):
        if validate_password(value) is not None:
            raise serializers.ValidationError("Senha inválida.")
        return make_password(value)

    def create(self, validated_data):
        nomes_grupos = validated_data.pop("groups")
        usuario = models.Usuario.objects.create(
            **validated_data, username=validated_data["email"]
        )
        usuario.groups.add(*Group.objects.filter(name__in=nomes_grupos))
        return usuario

    def update(self, usuario, validated_data):
        nomes_grupos = validated_data.pop("groups")

        for k, v in validated_data.items():
            setattr(usuario, k, v)

        usuario.groups.clear()
        usuario.groups.add(*Group.objects.filter(name__in=nomes_grupos))

        usuario.save()

        return usuario


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = ["linha_1", "cidade", "regiao", "pais", "codigo_postal"]


class EmpresaSerializer(serializers.ModelSerializer):
    cnpj = fields.CNPJField(
        label="CNPJ",
        validators=[
            validators.UniqueValidator(
                queryset=models.Empresa.objects.all(),
                message="Já existe uma empresa com este CNPJ.",
            )
        ],
    )
    endereco = EnderecoSerializer(allow_null=True, required=False)

    def create(self, validated_data):
        endereco_data = validated_data.pop("endereco", None)
        if endereco_data is None:
            endereco = None
        else:
            endereco, _ = models.Endereco.objects.get_or_create(**endereco_data)

        return models.Empresa.objects.create(**validated_data, endereco=endereco)

    def update(self, empresa, validated_data):
        endereco_data = validated_data.pop("endereco", None)
        if endereco_data is None:
            empresa.endereco = None
        else:
            empresa.endereco, _ = models.Endereco.objects.get_or_create(**endereco_data)

        for k, v in validated_data.items():
            setattr(empresa, k, v)

        empresa.save()

        return empresa

    class Meta:
        model = models.Empresa
        fields = [
            "id",
            "cnpj",
            "nome_fantasia",
            "razao_social",
            "email",
            "telefone",
            "endereco",
        ]
        read_only_fields = ["id"]


class TipoCargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoCarga
        fields = ["id", "nome", "unidade"]
        read_only_fields = ["id"]


class CargaSerializer(serializers.ModelSerializer):
    tipo = fields.PresentablePrimaryKeyRelatedField(
        queryset=models.TipoCarga.objects.all(),
        presentation_serializer_class=TipoCargaSerializer,
    )

    class Meta:
        model = models.Carga
        fields = ["quantidade", "tipo"]


class NavioSerializer(serializers.ModelSerializer):
    numero_imo = fields.IMONumberField(
        label="Número IMO",
        max_length=255,
        validators=[validators.UniqueValidator(queryset=models.Navio.objects.all())],
    )

    empresa = fields.PresentablePrimaryKeyRelatedField(
        queryset=models.Empresa.objects.all(),
        presentation_serializer_class=EmpresaSerializer,
    )
    tipos_de_carga_suportados = fields.PresentablePrimaryKeyRelatedField(
        queryset=models.TipoCarga.objects.all(),
        presentation_serializer_class=TipoCargaSerializer,
        required=False,
        many=True,
    )

    class Meta:
        model = models.Navio
        fields = [
            "numero_imo",
            "nome",
            "estado_bandeira",
            "comprimento_metros",
            "largura_metros",
            "numero_de_tripulantes",
            "porte_bruto_toneladas",
            "empresa",
            "tipos_de_carga_suportados",
        ]


class EmpresaNaviosListSerializer(serializers.ModelSerializer):
    numero_imo = fields.IMONumberField(label="Número IMO")
    tipos_de_carga_suportados = TipoCargaSerializer(many=True)

    class Meta:
        model = models.Navio
        fields = [
            "numero_imo",
            "nome",
            "estado_bandeira",
            "comprimento_metros",
            "largura_metros",
            "numero_de_tripulantes",
            "porte_bruto_toneladas",
            "tipos_de_carga_suportados",
        ]
        read_only_fields = fields


class PortoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    def create(self, validated_data):
        endereco_data = validated_data.pop("endereco", None)
        endereco, _ = models.Endereco.objects.get_or_create(**endereco_data)

        return models.Porto.objects.create(**validated_data, endereco=endereco)

    def update(self, porto, validated_data):
        endereco_data = validated_data.pop("endereco", None)
        porto.endereco, _ = models.Endereco.objects.get_or_create(**endereco_data)

        for k, v in validated_data.items():
            setattr(porto, k, v)

        porto.save()

        return porto

    class Meta:
        model = models.Porto
        fields = ["un_locode", "nome", "capacidade_teus_anuais", "endereco"]


class ViagemSerializer(serializers.ModelSerializer):
    navio = fields.PresentableSlugRelatedField(
        queryset=models.Navio.objects.all(),
        presentation_serializer_class=NavioSerializer,
        slug_field="numero_imo",
    )
    porto_origem = fields.PresentableSlugRelatedField(
        label="Porto de origem",
        queryset=models.Porto.objects.all(),
        presentation_serializer_class=PortoSerializer,
        slug_field="un_locode",
    )
    cargas = CargaSerializer(many=True)

    def create(self, validated_data):
        cargas_data = validated_data.pop("cargas", None)

        viagem = models.Viagem.objects.create(**validated_data)

        if cargas_data is not None:
            for carga_data in cargas_data:
                carga, _ = models.Carga.objects.get_or_create(
                    viagem=viagem, **carga_data
                )
                viagem.cargas.add(carga)

        viagem.save()

        return viagem

    def update(self, viagem, validated_data):
        cargas_data = validated_data.pop("cargas", None)
        viagem.cargas.all().delete()
        if cargas_data is not None:
            for carga_data in cargas_data:
                carga, _ = models.Carga.objects.get_or_create(
                    viagem=viagem, **carga_data
                )
                viagem.cargas.add(carga)

        for k, v in validated_data.items():
            setattr(viagem, k, v)

        viagem.save()

        return viagem

    def validate(self, data):
        if not (
            data["data_chegada"]
            <= data["data_atracacao"]
            <= data["data_liberacao"]
            <= data["data_saida"]
        ):
            raise serializers.ValidationError(
                "As datas devem estar em ordem cronológica."
            )
        return data

    class Meta:
        model = models.Viagem
        fields = [
            "codigo",
            "data_chegada",
            "data_atracacao",
            "data_liberacao",
            "data_saida",
            "navio",
            "porto_origem",
            "cargas",
        ]


class NavioViagensListSerializer(serializers.ModelSerializer):
    porto_origem = PortoSerializer()
    cargas = CargaSerializer(many=True)

    class Meta:
        model = models.Viagem
        fields = [
            "codigo",
            "data_chegada",
            "data_atracacao",
            "data_liberacao",
            "data_saida",
            "porto_origem",
            "cargas",
        ]
        read_only_fields = fields


class PortoViagensListSerializer(serializers.ModelSerializer):
    navio = NavioSerializer()
    cargas = CargaSerializer(many=True)

    class Meta:
        model = models.Viagem
        fields = [
            "codigo",
            "data_chegada",
            "data_atracacao",
            "data_liberacao",
            "data_saida",
            "navio",
            "cargas",
        ]
        read_only_fields = fields
