from functools import wraps
from flask import current_app
from flask_login import current_user, login_required


def is_current_user(tipo_desc):
    if current_user.is_anonymous:
        return False

    return current_user.tipo.descricao == tipo_desc


def tipo_usuario_required(tipo_desc):
    def decorator(func):
        @wraps(func)
        @login_required
        def inner(*args, **kwargs):
            if current_user.tipo.descricao == tipo_desc:
                return func(*args, **kwargs)
            return current_app.login_manager.unauthorized()
        return inner
    return decorator


def formatar_cpf(cpf, pontuacao=True):
    digitos = [x for x in cpf if x.isdigit()]
    if len(digitos) != 11:
        raise ValueError('CPF inválido')
    if pontuacao:
        return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*digitos)
    else:
        return ''.join(digitos)


def register_context_processors(app):
    @app.context_processor
    def _():
        return {
            'is_current_user': is_current_user
        }


def register_template_filters(app):
    @app.template_filter()
    def extract(item, container):
        value = container[item]
        return value

    app.add_template_filter(formatar_cpf)

