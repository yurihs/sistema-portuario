import pytest
from rest_framework import status

from sistema_portuario.core.models import Endereco, Porto


def criar_endereco(mimesis):
    return Endereco.objects.create(
        linha_1=mimesis("address.address"),
        cidade=mimesis("address.city"),
        regiao=mimesis("address.state"),
        pais=mimesis("address.country"),
        codigo_postal=mimesis("address.postal_code"),
    )


def gerar_endereco_dict(mimesis):
    return {
        "linha_1": mimesis("address.address"),
        "cidade": mimesis("address.city"),
        "regiao": mimesis("address.state"),
        "pais": mimesis("address.country"),
        "codigo_postal": mimesis("address.postal_code"),
    }


@pytest.mark.django_db
def test_list_portos(client, mimesis):
    porto_esperado = Porto.objects.create(
        un_locode=mimesis("address.country_code"),
        nome=mimesis("address.city"),
        endereco=criar_endereco(mimesis),
    )

    response = client.get("/api/portos/")
    assert response.status_code == status.HTTP_200_OK

    portos = response.json()
    assert len(portos) > 0

    porto_obtido = portos[0]
    assert porto_obtido["un_locode"] == porto_esperado.un_locode
    assert porto_obtido["nome"] == porto_esperado.nome
    assert porto_obtido["endereco"]["cidade"] == porto_esperado.endereco.cidade


@pytest.mark.django_db
def test_create_porto_valido(client, mimesis):
    contagem_inicial = Porto.objects.count()

    response = client.post(
        "/api/portos/",
        {
            "un_locode": mimesis("address.country_code"),
            "nome": mimesis("address.city"),
            "endereco": gerar_endereco_dict(mimesis),
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert "un_locode" in data

    contagem_final = Porto.objects.count()
    assert contagem_final == contagem_inicial + 1


@pytest.mark.django_db
def test_create_porto_duplicado(client, mimesis):
    porto_existente = Porto.objects.create(
        un_locode=mimesis("address.country_code"),
        nome=mimesis("address.city"),
        endereco=criar_endereco(mimesis),
    )
    contagem_inicial = Porto.objects.count()

    response = client.post(
        "/api/portos/",
        {
            "un_locode": porto_existente.un_locode,
            "nome": mimesis("address.city"),
            "endereco": gerar_endereco_dict(mimesis),
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "já existe" in ", ".join(data["un_locode"])

    contagem_final = Porto.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_update_porto_valido(client, mimesis):
    porto_original = Porto.objects.create(
        un_locode=mimesis("address.country_code"),
        nome=mimesis("address.city"),
        endereco=criar_endereco(mimesis),
    )

    novo_un_locode = mimesis("address.country_code")
    response = client.put(
        "/api/portos/{}/".format(porto_original.un_locode),
        {
            "un_locode": novo_un_locode,
            "nome": mimesis("address.city"),
            "endereco": gerar_endereco_dict(mimesis),
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK

    porto_alterado = Porto.objects.get(id=porto_original.id)
    assert porto_alterado.un_locode == novo_un_locode
