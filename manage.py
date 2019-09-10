import sys

from app import create_app, db
from app.models import TipoUsuario

app = create_app()


def criar_tipos_de_usuario():
    tipos = [
        'Administrador',
        'Funcionário',
    ]
    for tipo in tipos:
        db.session.add(TipoUsuario(descricao=tipo))
    db.session.commit()


def initdb():
    db.drop_all()
    db.create_all()
    criar_tipos_de_usuario()
    db.session.commit()


def print_usage():
    print('Usage:')
    print(sys.argv[0], 'initdb')


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    with app.app_context():
        command = sys.argv[1]
        if command == 'initdb' and len(sys.argv) == 2:
            initdb()
            print('O banco de dados for inicializado:', app.config['SQLALCHEMY_DATABASE_URI'])


if __name__ == '__main__':
    main()
