import os
import pytest

from mimesis import Generic
from mimesis.builtins import BrazilSpecProvider

from app import create_app, db
from app.models import TipoUsuario


@pytest.fixture
def client():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    client = app.test_client()

    with app.app_context():
        db.drop_all()
        db.create_all()
        tipos = [
            'Administrador',
            'Funcionário',
        ]
        for tipo in tipos:
            db.session.add(TipoUsuario(descricao=tipo))
        db.session.commit()

    yield client


@pytest.fixture
def mimesis():
    generic = Generic('pt-br')
    BrazilSpecProvider.Meta.name = 'brasil'
    generic.add_provider(BrazilSpecProvider)
    yield generic
