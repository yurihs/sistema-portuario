from flask import Blueprint, render_template

usuario = Blueprint('usuario', __name__)


@usuario.route('/')
def listar_usuarios():
    return render_template('usuarios/lista.html')

@usuario.route('/<int:id_usuario>')
def editar(id_usuario):
    pass

