from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from app import db
from app.models import Usuario
from app.validators import CPF

tipos_usuario = {
    1: 'Funcionário',
    2: 'Administrador'
}

usuario = Blueprint('usuario', __name__)


@usuario.route('/')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)


class UsuarioCadastrarForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email')
    cpf = StringField('cpf', validators=[CPF()])
    tipo = SelectField('tipo', choices=list(tipos_usuario.items()), coerce=int)
    senha = StringField('senha', validators=[DataRequired()])
    confirmar_senha = StringField('confirmar_senha', validators=[DataRequired()])


@usuario.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = UsuarioCadastrarForm()
    if form.is_submitted():
        if form.validate():
            usuario = Usuario(
                nome=form.nome.data,
                email=form.email.data,
                cpf=''.join(x for x in form.cpf.data if x.isdigit()),
                hash_senha=form.senha.data
            )
            db.session.add(usuario)
            db.session.commit()
            flash('Usuário criado com sucesso.', 'success')
            return redirect(url_for('usuario.listar_usuarios'))

    return render_template('usuarios/cadastrar.html', form=form, tipos_usuario=tipos_usuario)




@usuario.route('/<int:id_usuario>')
def editar(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    return render_template('usuarios/editar.html', usuario=usuario)


@usuario.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email is None or senha is None:
            flash('Usuário inválido')
            return render_template('usuarios/login.html')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario is None:
            flash('Usuário inválido')
            return render_template('usuarios/login.html')

        # TODO Autenticar (verificar senha)

        login_user(usuario)
        return redirect(url_for('usuario.listar_usuarios'))

    return render_template('usuarios/login.html')
