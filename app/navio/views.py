from flask import Blueprint, render_template

from app.empresa.views import empresas

navio = Blueprint('navio', __name__)

navios = [
    dict(
        id=1,
        nome='MAERSK LIRQUEN',
        numero_imo='9526887',
        comprimento_m=300,
        porte_bruto_t=106043,
        bandeira='Hong Kong',
        n_tripulantes=40,
        empresa=dict(id=2, razao_social='Maersk Brasil Brasmar Ltda.')
    ),
    dict(
        id=2,
        nome='CMA CGM RIO GRANDE',
        numero_imo='9722699',
        comprimento_m=300,
        porte_bruto_t=110521,
        bandeira='Malta',
        n_tripulantes=37,
        empresa=dict(id=4, razao_social='CMA CGM do Brasil Agência Marítima Ltda.')
    ),
    dict(
        id=3,
        nome='MONTE TAMARO',
        numero_imo='9357949',
        comprimento_m=272,
        porte_bruto_t=71587,
        bandeira='Singapura',
        n_tripulantes=22,
        empresa=dict(id=3, razao_social='Aliança Navegação e Logística Ltda.')
    ),
    dict(
        id=4,
        nome='PEDRO ALVARES CABRAL',
        numero_imo='9603219',
        comprimento_m=228,
        porte_bruto_t=52019,
        bandeira='Brasil',
        n_tripulantes=20,
        empresa=dict(id=3, razao_social='Aliança Navegação e Logística Ltda.')
    )
]


@navio.route('/')
def listar():
    return render_template('navio/listar.html', navios=navios)


@navio.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return render_template('navio/cadastrar.html', empresas=empresas)


@navio.route('/<int:id_navio>')
def editar(id_navio):
    navio = navios[id_navio-1]
    return render_template('navio/editar.html', navio=navio, empresas=empresas)
