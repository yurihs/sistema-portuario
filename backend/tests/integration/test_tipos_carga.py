import pytest
from rest_framework import status

from sistema_portuario.core.models import TipoCarga


@pytest.mark.django_db
def test_list_tipos_carga(client, mimesis):
    tipo_carga_esperado = TipoCarga.objects.create(
        nome=mimesis("food.vegetable"), unidade=mimesis("unit_system.unit", symbol=True)
    )

    response = client.get("/api/tipos-carga/")
    assert response.status_code == status.HTTP_200_OK

    tipos_carga = response.json()
    assert len(tipos_carga) > 0

    tipo_carga_obtido = tipos_carga[0]
    assert tipo_carga_obtido["nome"] == tipo_carga_esperado.nome
    assert tipo_carga_obtido["unidade"] == tipo_carga_esperado.unidade


@pytest.mark.django_db
def test_create_tipo_carga_valido(client, mimesis):
    contagem_inicial = TipoCarga.objects.count()

    response = client.post(
        "/api/tipos-carga/",
        {
            "nome": mimesis("food.vegetable"),
            "unidade": mimesis("unit_system.unit", symbol=True),
        },
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert "id" in data

    contagem_final = TipoCarga.objects.count()
    assert contagem_final == contagem_inicial + 1


@pytest.mark.django_db
def test_create_tipo_carga_duplicado(client, mimesis):
    tipo_carga_existente = TipoCarga.objects.create(
        nome=mimesis("food.vegetable"), unidade=mimesis("unit_system.unit", symbol=True)
    )
    contagem_inicial = TipoCarga.objects.count()

    response = client.post(
        "/api/tipos-carga/",
        {
            "nome": tipo_carga_existente.nome,
            "unidade": mimesis("unit_system.unit", symbol=True),
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "já existe" in ", ".join(data["nome"])

    contagem_final = TipoCarga.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_update_tipo_carga_valido(client, mimesis):
    tipo_carga_original = TipoCarga.objects.create(
        nome=mimesis("food.vegetable"), unidade=mimesis("unit_system.unit", symbol=True)
    )

    novo_nome = mimesis("food.vegetable")
    response = client.put(
        "/api/tipos-carga/{}/".format(tipo_carga_original.id),
        {"nome": novo_nome, "unidade": tipo_carga_original.unidade},
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK

    tipo_carga_alterado = TipoCarga.objects.get(id=tipo_carga_original.id)
    assert tipo_carga_alterado.nome == novo_nome
