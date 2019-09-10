from flask_login import current_user

from app import db
from app.models import Usuario


def cadastrar_usuario(client, mimesis):
    email = mimesis.person.email()
    senha = mimesis.person.password()
    client.post('/usuarios/cadastrar', data={
        'nome': mimesis.person.full_name(),
        'email': email,
        'cpf': mimesis.brasil.cpf(),
        'senha': senha,
        'confirmar_senha': senha,
    })
    usuario = Usuario.query.filter_by(email=email).first()
    db.session.expunge(usuario)
    return usuario, senha


def login(client, email, password):
    return client.post('/usuarios/login', data={
        'email': email,
        'senha': password,
    })


def test_login_valido(client, mimesis):
    with client:
        u, senha = cadastrar_usuario(client, mimesis)
        assert current_user.is_anonymous

        login(client, u.email, senha)
        assert not current_user.is_anonymous
        assert current_user.email == u.email


def test_login_invalido(client, mimesis):
    with client:
        u, senha = cadastrar_usuario(client, mimesis)
        assert current_user.is_anonymous
        login(client, u.email + 'errado', senha + 'errada')
        assert current_user.is_anonymous
