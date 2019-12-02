from datetime import timedelta

import pytest
from rest_framework import status

from sistema_portuario.core.models import (
    Empresa,
    Endereco,
    Navio,
    Porto,
    TipoCarga,
    Viagem,
)
from sistema_portuario.core.utils import gerar_numero_imo


def criar_empresa(mimesis):
    return Empresa.objects.create(
        cnpj=mimesis("brasil.cnpj", with_mask=False),
        nome_fantasia=mimesis("business.company"),
        razao_social=mimesis("business.company"),
    )


def criar_navio(mimesis):
    return Navio.objects.create(
        numero_imo=gerar_numero_imo(),
        nome=mimesis("person.name"),
        estado_bandeira=mimesis("address.country_code"),
        empresa=criar_empresa(mimesis),
    )


def criar_endereco(mimesis):
    return Endereco.objects.create(
        linha_1=mimesis("address.address"),
        cidade=mimesis("address.city"),
        regiao=mimesis("address.state"),
        pais=mimesis("address.country"),
        codigo_postal=mimesis("address.postal_code"),
    )


def criar_porto(mimesis):
    return Porto.objects.create(
        un_locode=mimesis("address.country_code"),
        nome=mimesis("address.city"),
        endereco=criar_endereco(mimesis),
    )


def criar_tipo_carga(mimesis):
    return TipoCarga.objects.create(
        nome=mimesis("food.vegetable"),
        unidade=mimesis("unit_system.unit", symbol=True),
    )


@pytest.mark.django_db
def test_list_viagens(client, mimesis):
    viagem_esperada = Viagem.objects.create(
        codigo="001", navio=criar_navio(mimesis), porto_origem=criar_porto(mimesis)
    )

    response = client.get("/api/viagens/")
    assert response.status_code == status.HTTP_200_OK

    viagens = response.json()
    assert len(viagens) > 0

    viagem_obtida = viagens[0]
    assert viagem_obtida["codigo"] == viagem_esperada.codigo
    assert viagem_obtida["navio"]["numero_imo"] == viagem_esperada.navio.numero_imo
    assert (
        viagem_obtida["porto_origem"]["un_locode"]
        == viagem_esperada.porto_origem.un_locode
    )


@pytest.mark.django_db
def test_create_viagem_valida(client, mimesis):
    navio = criar_navio(mimesis)
    porto = criar_porto(mimesis)
    tipo_carga = criar_tipo_carga(mimesis)

    contagem_inicial = Viagem.objects.count()

    data_chegada = mimesis("datetime.datetime")

    response = client.post(
        "/api/viagens/",
        {
            "codigo": "001",
            "navio": navio.numero_imo,
            "porto_origem": porto.un_locode,
            "data_chegada": data_chegada,
            "data_atracacao": data_chegada + timedelta(hours=1),
            "data_liberacao": data_chegada + timedelta(hours=2),
            "data_saida": data_chegada + timedelta(hours=3),
            "cargas": [{"tipo": tipo_carga.id, "quantidade": 10}],
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert "codigo" in data

    contagem_final = Viagem.objects.count()
    assert contagem_final == contagem_inicial + 1


@pytest.mark.django_db
def test_create_viagem_invalida(client, mimesis):
    contagem_inicial = Viagem.objects.count()

    data_chegada = mimesis("datetime.datetime")

    response = client.post(
        "/api/viagens/",
        {
            "codigo": "001",
            "navio": 999,
            "porto_origem": 999,
            "data_chegada": data_chegada,
            "data_atracacao": data_chegada + timedelta(hours=9),
            "data_liberacao": data_chegada + timedelta(hours=1),
            "data_saida": data_chegada + timedelta(hours=4),
            "cargas": [],
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "não existe" in ", ".join(data["navio"])
    assert "não existe" in ", ".join(data["porto_origem"])

    contagem_final = Viagem.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_update_viagem_valida(client, mimesis):
    viagem_original = Viagem.objects.create(
        codigo="001", navio=criar_navio(mimesis), porto_origem=criar_porto(mimesis)
    )

    tipo_carga = criar_tipo_carga(mimesis)
    data_chegada = mimesis("datetime.datetime")

    novo_codigo = "002"
    response = client.put(
        "/api/viagens/{}/".format(viagem_original.id),
        {
            "codigo": novo_codigo,
            "navio": viagem_original.navio.numero_imo,
            "porto_origem": viagem_original.porto_origem.un_locode,
            "data_chegada": data_chegada,
            "data_atracacao": data_chegada + timedelta(hours=1),
            "data_liberacao": data_chegada + timedelta(hours=2),
            "data_saida": data_chegada + timedelta(hours=3),
            "cargas": [{"tipo": tipo_carga.id, "quantidade": 10}],
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK

    viagem_alterada = Viagem.objects.get(id=viagem_original.id)
    assert viagem_alterada.codigo == novo_codigo
    assert viagem_alterada.cargas.filter(tipo__id=tipo_carga.id).exists()
