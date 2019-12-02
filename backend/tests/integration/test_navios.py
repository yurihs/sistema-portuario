import pytest
from rest_framework import status

from sistema_portuario.core.models import Empresa, Navio
from sistema_portuario.core.utils import gerar_numero_imo


def criar_empresa(mimesis):
    return Empresa.objects.create(
        cnpj=mimesis("brasil.cnpj", with_mask=False),
        nome_fantasia=mimesis("business.company"),
        razao_social=mimesis("business.company"),
    )


@pytest.mark.django_db
def test_list_navios(client, mimesis):
    navio_esperado = Navio.objects.create(
        numero_imo=gerar_numero_imo(),
        nome=mimesis("person.name"),
        estado_bandeira=mimesis("address.country_code"),
        empresa=criar_empresa(mimesis),
    )

    response = client.get("/api/navios/")
    assert response.status_code == status.HTTP_200_OK

    navios = response.json()
    assert len(navios) > 0

    navio_obtido = navios[0]
    assert navio_obtido["numero_imo"] == navio_esperado.numero_imo
    assert navio_obtido["nome"] == navio_esperado.nome
    assert navio_obtido["estado_bandeira"] == navio_esperado.estado_bandeira
    assert navio_obtido["empresa"]["id"] == navio_esperado.empresa.id


@pytest.mark.django_db
def test_create_navio_valido(client, mimesis):
    empresa = criar_empresa(mimesis)
    contagem_inicial = Navio.objects.count()

    response = client.post(
        "/api/navios/",
        {
            "numero_imo": gerar_numero_imo(),
            "nome": mimesis("person.name"),
            "estado_bandeira": mimesis("address.country_code"),
            "empresa": empresa.id,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert "numero_imo" in data

    contagem_final = Navio.objects.count()
    assert contagem_final == contagem_inicial + 1


@pytest.mark.django_db
def test_create_navio_invalido(client, mimesis):
    contagem_inicial = Navio.objects.count()

    response = client.post(
        "/api/navios/",
        {
            "numero_imo": "um número imo inválido",
            "nome": mimesis("person.name"),
            "estado_bandeira": mimesis("address.country_code"),
            "empresa": 999,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "Número IMO inválido." in data["numero_imo"]
    assert "não existe" in ", ".join(data["empresa"])

    contagem_final = Navio.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_create_navio_duplicado(client, mimesis):
    empresa = criar_empresa(mimesis)

    navio_existente = Navio.objects.create(
        numero_imo=gerar_numero_imo(),
        nome=mimesis("person.name"),
        estado_bandeira=mimesis("address.country_code"),
        empresa=empresa,
    )
    contagem_inicial = Navio.objects.count()

    response = client.post(
        "/api/navios/",
        {
            "numero_imo": navio_existente.numero_imo,
            "nome": mimesis("person.name"),
            "estado_bandeira": mimesis("address.country_code"),
            "empresa": empresa.id,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "Esse campo deve ser  único." in data["numero_imo"]

    contagem_final = Navio.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_update_navio_valido(client, mimesis):
    empresa = criar_empresa(mimesis)

    navio_original = Navio.objects.create(
        numero_imo=gerar_numero_imo(),
        nome=mimesis("person.name"),
        estado_bandeira=mimesis("address.country_code"),
        empresa=empresa,
    )

    novo_numero_imo = gerar_numero_imo()
    response = client.put(
        "/api/navios/{}/".format(navio_original.numero_imo),
        {
            "numero_imo": novo_numero_imo,
            "nome": navio_original.nome,
            "estado_bandeira": navio_original.estado_bandeira,
            "empresa": empresa.id,
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK

    navio_alterado = Navio.objects.get(id=navio_original.id)
    assert navio_alterado.numero_imo == novo_numero_imo
