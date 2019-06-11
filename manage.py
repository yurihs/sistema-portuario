import sys

from app import create_app, db
from app.models import Usuario

app = create_app()


def initdb():
    db.drop_all()
    db.create_all()
    db.session.commit()


def createadmin(nome, email, senha):
    usuario = Usuario(
        nome=nome,
        email=email,
        hash_senha=senha
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario


def print_usage():
    print('Usage:')
    print(sys.argv[0], 'initdb')
    print(sys.argv[0], 'createadmin')


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    with app.app_context():
        command = sys.argv[1]
        if command == 'initdb' and len(sys.argv) == 2:
            initdb()
            print('O banco de dados for inicializado:', app.config['SQLALCHEMY_DATABASE_URI'])
        elif command == 'createadmin':
            nome = input('Nome [Administrador]:') or 'Administrador'
            email = input('E-mail [admin@example.com]:') or 'admin@example.com'
            senha = input('Senha [admin]: ') or 'admin'
            admin = createadmin(nome, email, senha)
            print('O usuário administrador "{:}" foi criado.'.format(admin.email))


if __name__ == '__main__':
    main()
