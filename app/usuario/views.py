from flask import Blueprint, abort, flash, render_template, request, redirect, url_for
from flask_login import login_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional

from app import db
from app.models import Usuario, TipoUsuario
from app.fields import CPFField
from app.utils import is_current_user

usuario = Blueprint('usuario', __name__)


@usuario.route('/')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)


class UsuarioCadastrarForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email')
    cpf = CPFField('cpf')
    senha = StringField('senha', validators=[DataRequired()])
    confirmar_senha = StringField('confirmar_senha', validators=[DataRequired()])


class UsuarioEditarForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email')
    cpf = CPFField('cpf')
    tipo = IntegerField('tipo', validators=[Optional()])


@usuario.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = UsuarioCadastrarForm()
    if form.is_submitted():
        if form.validate():
            is_primeiro_usuario = Usuario.query.count() == 0
            # O primeiro usuário cadastrado será um administrador
            if is_primeiro_usuario:
                tipo_desc = 'Administrador'
            # Os outros são funcionários, por padrão
            else:
                tipo_desc = 'Funcionário'
            tipo = TipoUsuario.query.filter_by(descricao=tipo_desc).first()

            usuario = Usuario(
                nome=form.nome.data,
                email=form.email.data,
                cpf=form.cpf.data,
                hash_senha=form.senha.data,
                tipo=tipo,
            )

            db.session.add(usuario)
            db.session.commit()
            flash('Usuário criado com sucesso.', 'success')
            return redirect(url_for('usuario.listar_usuarios'))

    return render_template('usuarios/cadastrar.html', form=form)


@usuario.route('/<int:id_usuario>', methods=['GET', 'POST'])
def editar(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    if usuario is None:
        abort(404)


    if not is_current_user('Administrador') and current_user.id != usuario.id:
        abort(403)

    form = UsuarioEditarForm()
    if form.is_submitted():
        if form.validate():
            usuario.nome = form.nome.data
            usuario.email = form.email.data
            usuario.cpf = form.cpf.data

            if is_current_user('Administrador') and form.tipo.data is not None:
                tipo = TipoUsuario.query.get(form.tipo.data)
                usuario.tipo = tipo

            db.session.commit()
            flash('Usuário "{:s}" modificado com sucesso.'.format(usuario.nome), 'success')
            return redirect(url_for('usuario.listar_usuarios'))
    tipos_usuario = TipoUsuario.query.all()
    return render_template('usuarios/editar.html', form=form, usuario=usuario, tipos_usuario=tipos_usuario)


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
