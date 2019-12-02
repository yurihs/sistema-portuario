import pytest
from rest_framework import status

from sistema_portuario.core.models import Empresa


@pytest.mark.django_db
def test_list_empresas(client, mimesis):
    empresa_esperada = Empresa.objects.create(
        cnpj=mimesis("brasil.cnpj", with_mask=False),
        nome_fantasia=mimesis("business.company"),
        razao_social=mimesis("business.company"),
    )

    response = client.get("/api/empresas/")
    assert response.status_code == status.HTTP_200_OK

    empresas = response.json()
    assert len(empresas) > 0

    empresa_obtida = empresas[0]
    cpf_obtido_apenas_digitos = "".join(
        x for x in empresa_obtida["cnpj"] if x.isdigit()
    )
    assert cpf_obtido_apenas_digitos == empresa_esperada.cnpj
    assert empresa_obtida["nome_fantasia"] == empresa_esperada.nome_fantasia
    assert empresa_obtida["razao_social"] == empresa_esperada.razao_social


@pytest.mark.django_db
def test_create_empresa_valida(client, mimesis):
    contagem_inicial = Empresa.objects.count()

    response = client.post(
        "/api/empresas/",
        {
            "cnpj": mimesis("brasil.cnpj"),
            "nome_fantasia": mimesis("business.company"),
            "razao_social": mimesis("business.company"),
        },
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert "id" in data

    contagem_final = Empresa.objects.count()
    assert contagem_final == contagem_inicial + 1


@pytest.mark.django_db
def test_create_empresa_invalida(client, mimesis):
    contagem_inicial = Empresa.objects.count()

    response = client.post(
        "/api/empresas/",
        {
            "cnpj": "um cnpj inválido",
            "nome_fantasia": mimesis("business.company"),
            "razao_social": mimesis("business.company"),
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "CNPJ inválido." in data["cnpj"]

    contagem_final = Empresa.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_create_empresa_duplicada(client, mimesis):
    empresa_existente = Empresa.objects.create(
        cnpj=mimesis("brasil.cnpj", with_mask=False),
        nome_fantasia=mimesis("business.company"),
        razao_social=mimesis("business.company"),
    )
    contagem_inicial = Empresa.objects.count()

    response = client.post(
        "/api/empresas/",
        {
            "cnpj": empresa_existente.cnpj,
            "nome_fantasia": mimesis("business.company"),
            "razao_social": mimesis("business.company"),
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "Já existe uma empresa com este CNPJ." in data["cnpj"]

    contagem_final = Empresa.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_update_empresa_valida(client, mimesis):
    empresa_original = Empresa.objects.create(
        cnpj=mimesis("brasil.cnpj", with_mask=False),
        nome_fantasia=mimesis("business.company"),
        razao_social=mimesis("business.company"),
    )

    novo_cnpj = mimesis("brasil.cnpj", with_mask=False)
    response = client.put(
        "/api/empresas/{}/".format(empresa_original.id),
        {
            "cnpj": novo_cnpj,
            "nome_fantasia": empresa_original.nome_fantasia,
            "razao_social": empresa_original.razao_social,
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK

    empresa_alterada = Empresa.objects.get(id=empresa_original.id)
    assert empresa_alterada.cnpj == novo_cnpj
