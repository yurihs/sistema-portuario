import pytest
from rest_framework import status

from sistema_portuario.core.models import Usuario


@pytest.mark.django_db
def test_list_usuarios(client):
    response = client.get("/api/usuarios/")
    assert response.status_code == status.HTTP_200_OK

    usuarios = response.json()
    assert len(usuarios) > 0

    admin = usuarios[0]
    assert admin["email"] == "admin@example.com"


@pytest.mark.django_db
def test_create_usuario_valido(client, mimesis):
    contagem_inicial = Usuario.objects.count()

    response = client.post(
        "/api/usuarios/",
        {
            "email": "user@example.com",
            "password": mimesis("person.password"),
            "cpf": mimesis("brasil.cpf"),
            "grupo": "Funcionários",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert "id" in data

    contagem_final = Usuario.objects.count()
    assert contagem_final == contagem_inicial + 1


@pytest.mark.django_db
def test_create_usuario_invalido(client, mimesis):
    contagem_inicial = Usuario.objects.count()

    response = client.post(
        "/api/usuarios/",
        {
            "email": "um email inválido",
            "cpf": "um cpf inválido",
            "grupo": "um grupo inválido",
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert "CPF inválido." in data["cpf"]
    assert "Insira um endereço de email válido." in data["email"]
    assert "Grupo inválido." in data["grupo"]
    assert "Este campo é obrigatório." in data["password"]

    contagem_final = Usuario.objects.count()
    assert contagem_final == contagem_inicial


@pytest.mark.django_db
def test_update_usuario_valido(client, mimesis):
    novo_cpf = mimesis("brasil.cpf", with_mask=False)
    response = client.put(
        "/api/usuarios/1/",
        {
            "email": "admin@example.com",
            "password": mimesis("person.password"),
            "cpf": novo_cpf,
            "grupo": "Administradores",
        },
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK

    admin = Usuario.objects.get(id=1)
    assert admin.cpf == novo_cpf
