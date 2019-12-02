import pytest

from sistema_portuario.core.models import Empresa
from sistema_portuario.core.serializers import NavioSerializer


def criar_empresa(mimesis):
    return Empresa.objects.create(
        cnpj=mimesis("brasil.cnpj", with_mask=False),
        nome_fantasia=mimesis("business.company"),
        razao_social=mimesis("business.company"),
    )


@pytest.mark.django_db
def test_valid(mimesis):
    empresa = criar_empresa(mimesis)

    input_data = {
        "numero_imo": "6711883",
        "nome": mimesis("address.city"),
        "estado_bandeira": mimesis("address.country_code"),
        "empresa": empresa.id,
    }

    serializer = NavioSerializer(data=input_data)
    assert serializer.is_valid()
    output_data = serializer.validated_data

    assert output_data["nome"] == input_data["nome"]
    assert output_data["empresa"].cnpj == empresa.cnpj


@pytest.mark.django_db
def test_invalid(mimesis):
    input_data = {
        "numero_imo": "1111883",
        "nome": mimesis("address.city"),
        "estado_bandeira": mimesis("address.country_code"),
        "empresa": 999,
    }

    serializer = NavioSerializer(data=input_data)
    assert not serializer.is_valid()

    assert "numero_imo" in serializer.errors
    assert "empresa" in serializer.errors
