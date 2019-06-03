from flask import Blueprint, render_template

usuario = Blueprint('usuario', __name__)

usuarios = [
    dict(id=1, nome='Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr.', email="hubertbw@example.com", cpf='109.985.380-00', tipo='Administrador'),
    dict(id=2, nome='Fulano da Silva', email="fulanos@example.com", cpf='796.520.230-19', tipo='Funcionário'),
    dict(id=3, nome='Alice', email="alice@example.com", cpf='832.557.570-02', tipo='Funcionário'),
    dict(id=4, nome='Bob', email="bob@example.com", cpf='902.795.460-76', tipo='Funcionário'),
    dict(id=5, nome='Charlie', email="charlie@example.com", cpf='882.450.240-74', tipo='Funcionário'),
    dict(id=6, nome='Dave', email="dave@example.com", cpf='540.911.310-18', tipo='Funcionário'),
]


@usuario.route('/')
def listar_usuarios():
    return render_template('usuarios/listar.html', usuarios=usuarios)


@usuario.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return render_template('usuarios/cadastrar.html')


@usuario.route('/<int:id_usuario>')
def editar(id_usuario):
    usuario = usuarios[id_usuario-1]
    return render_template('usuarios/editar.html', usuario=usuario)
