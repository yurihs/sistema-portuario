import pytest

from sistema_portuario.core.serializers import EmpresaSerializer


@pytest.mark.django_db
def test_valida(mimesis):
    cnpj_com_mascara = mimesis("brasil.cnpj")
    cnpj_sem_mascara = "".join(x for x in cnpj_com_mascara if x.isdigit())

    input_data = {
        "cnpj": cnpj_com_mascara,
        "nome_fantasia": mimesis("business.company"),
        "razao_social": mimesis("business.company"),
    }

    serializer = EmpresaSerializer(data=input_data)
    assert serializer.is_valid()
    output_data = serializer.validated_data

    assert output_data["cnpj"] == cnpj_sem_mascara
    assert output_data["nome_fantasia"] == input_data["nome_fantasia"]
    assert output_data["razao_social"] == input_data["razao_social"]


@pytest.mark.django_db
def test_invalida(mimesis):
    input_data = {
        "cnpj": "11.791.882/0001-11",
        "nome_fantasia": mimesis("business.company"),
        "razao_social": mimesis("business.company"),
    }

    serializer = EmpresaSerializer(data=input_data)

    assert not serializer.is_valid()
    assert "cnpj" in serializer.errors
