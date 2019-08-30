from datetime import datetime
from flask import Blueprint, render_template

from app.porto.views import portos
from app.navio.views import navios

viagem = Blueprint('viagem', __name__)

viagens = [
    {
        'id': 1,
        'codigo': 'LIRQ343',
        'navio':          dict(nome='MAERSK LIRQUEN'),
        'porto_origem':   dict(nome='Porto de Itaguaí'),
        'data_chegada':   datetime(2019, 8, 28, 10,  0,  0),
        'data_atracacao': datetime(2019, 8, 28, 11,  0,  0),
        'data_liberacao': datetime(2019, 8, 28, 23,  0,  0),
        'data_saida':     datetime(2019, 8, 28, 23, 10,  1),
    },
    {
        'id': 2,
        'codigo': 'LIRQ344',
        'navio':          dict(nome='MAERSK LIRQUEN'),
        'porto_origem':   dict(nome='Porto de Itaguaí'),
        'data_chegada':   datetime(2019, 8, 10, 12,  0,  0),
        'data_atracacao': datetime(2019, 8, 10, 12, 54,  2),
        'data_liberacao': datetime(2019, 8, 12, 10,  0,  0),
        'data_saida':     datetime(2019, 8, 12, 20,  0,  0),
    },
    {
        'id': 3,
        'codigo': 'RIOG394',
        'navio':          dict(nome='CMA CGM RIO GRANDE'),
        'porto_origem':   dict(nome='Porto de Itapoá'),
        'data_chegada':   datetime(2019, 8, 10,  1,  0,  0),
        'data_atracacao': datetime(2019, 8, 10, 20,  0, 25),
        'data_liberacao': datetime(2019, 8, 12,  0,  0,  0),
        'data_saida':     datetime(2019, 8, 12,  0, 30,  4),
    },
    {
        'id': 4,
        'codigo': 'PEDRO356',
        'navio':          dict(nome='PEDRO ALVARES CABRAL'),
        'porto_origem':   dict(nome='Porto de Barra do Riacho'),
        'data_chegada':   datetime(2019, 8,  7, 23, 32,  0),
        'data_atracacao': datetime(2019, 8,  8,  0,  5,  0),
        'data_liberacao': datetime(2019, 8,  8,  5,  5,  0),
        'data_saida':     datetime(2019, 8,  8,  6,  0,  0),
    },
    {
        'id': 5,
        'codigo': 'MONT266',
        'navio':           dict(nome='MONTE TAMARO'),
        'porto_origem':    dict(nome='Porto de Barra do Riacho'),
        'data_chegada':    datetime(2019, 8,  4, 12, 30,  0),
        'data_atracacao':  datetime(2019, 8,  5,  6,  0,  0),
        'data_liberacao':  datetime(2019, 8,  5, 12,  0,  0),
        'data_saida':      datetime(2019, 8,  5, 12, 22,  0),
    },
    {
        'id': 6,
        'codigo': 'MONT263',
        'navio':          dict(nome='MONTE TAMARO'),
        'porto_origem':   dict(nome='Porto de Salvador'),
        'data_chegada':   datetime(2019, 8,  3, 18,  0,  0),
        'data_atracacao': datetime(2019, 8,  3, 18, 50,  0),
        'data_liberacao': datetime(2019, 8,  3, 23, 30,  0),
        'data_saida':     datetime(2019, 8,  4,  7,  0,  0),
    },
]


@viagem.route('/')
def listar_usuarios():
    return render_template('viagem/listar.html', viagens=viagens)


@viagem.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return render_template('viagem/cadastrar.html', navios=navios, portos=portos)


@viagem.route('/<int:id_viagem>')
def editar(id_viagem):
    viagem = viagens[id_viagem-1]
    return render_template('viagem/editar.html', viagem=viagem, navios=navios, portos=portos)
