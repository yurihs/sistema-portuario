import pytest

from sistema_portuario.core.serializers import PortoSerializer


@pytest.mark.django_db
def test_valid(mimesis):
    input_data = {
        "un_locode": mimesis("address.country_code"),
        "nome": mimesis("address.city"),
        "endereco": {
            "linha_1": mimesis("address.address"),
            "cidade": mimesis("address.city"),
            "regiao": mimesis("address.state"),
            "pais": mimesis("address.country"),
            "codigo_postal": mimesis("address.postal_code"),
        },
    }

    serializer = PortoSerializer(data=input_data)
    assert serializer.is_valid(raise_exception=True)
    output_data = serializer.validated_data

    assert output_data["un_locode"] == input_data["un_locode"]
    assert output_data["nome"] == input_data["nome"]
    assert output_data["endereco"]["cidade"] == input_data["endereco"]["cidade"]


@pytest.mark.django_db
def test_invalid(mimesis):
    input_data = {
        "un_locode": mimesis("address.country_code"),
    }

    serializer = PortoSerializer(data=input_data)
    assert not serializer.is_valid()

    assert "nome" in serializer.errors
    assert "endereco" in serializer.errors
