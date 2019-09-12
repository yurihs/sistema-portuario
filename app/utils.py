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


def validar_imo(imo):
    '''
    Este é constituído por um número de seis dígitos sequenciais únicos
    seguido por um dígito de verificação. A integridade de um número IMO pode
    ser verificada usando o seu dígito de verificação. Isto é feito multiplicando
    cada um dos primeiros seis dígitos por um fator de 2 para 7 correspondente à
    posição da direita para a esquerda. O dígito mais à direita dessa soma é o dígito
    de verificação. Por exemplo, para IMO 9074729: 
    (9×7) + (0×6) + (7x5) + (4×4) + (7×3) + (2×2) = 139
    '''
    if len(imo) != 7:
        return False

    try:
        # separar digitos posicionais do verificador em ordem reversa
        # por exemplo "3074729", pos ficará 274703, verificador igual a 9
        pos = map(int, imo[-2::-1])
        verificador = imo[-1]
        soma = sum(p*i for p, i in enumerate(pos, start=2))
    except ValueError:
        return False

    return str(soma)[-1] == verificador
