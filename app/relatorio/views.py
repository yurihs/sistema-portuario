import random

from datetime import datetime
from flask import Blueprint, render_template, request, flash

from app.empresa.views import empresas
from app.navio.views import navios
from app.porto.views import portos

relatorio = Blueprint('relatorio', __name__)


@relatorio.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('relatorio/index.html', empresas=empresas)

    try:
        data_inicio = datetime.strptime(request.form.get('data_inicio'), '%Y-%m-%d').date()
        data_termino = datetime.strptime(request.form.get('data_termino'), '%Y-%m-%d').date()
    except (ValueError, TypeError) as e:
        flash("Informe as datas de início e de término.")
        return render_template('relatorio/index.html', empresas=empresas)

    tipo_relatorio = request.form.get('tipo_relatorio')
    if tipo_relatorio == 'geral':
        return gerar_relatorio_geral(data_inicio, data_termino)
    elif tipo_relatorio == 'especifico':
        try:
            id_empresa = int(request.form.get('empresa'))
            return gerar_relatorio_especifico(data_inicio, data_termino, id_empresa)
        except (ValueError, TypeError):
            flash("Selecione uma empresa.")
    else:
        flash("Selecione um tipo de relatório.")

    return render_template('relatorio/index.html', empresas=empresas)


def gerar_relatorio_geral(data_inicio, data_termino):
    empresas_to_n_viagens = {
        empresa['nome_fantasia'] or empresa['razao_social']: random.randrange(80)
        for empresa in empresas
    }

    tipo_de_carga_to_cor = {
        'Contêiner': '#66c2a5',
        'Reefer': '#8da0cb',
        'Granel': '#fc8d62',
    }

    empresas_to_tipo_de_carga = {
        empresa['nome_fantasia'] or empresa['razao_social']: {
            'Contêiner': random.randrange(80),
            'Reefer': random.randrange(80),
            'Granel': random.randrange(80)
        }
        for empresa in empresas
    }

    tipo_de_carga_to_qty = {
        tipo: random.randrange(80)
        for tipo in tipo_de_carga_to_cor.keys()
    }

    total_n_viagens = sum(empresas_to_n_viagens.values())
    total_n_navios = 0 if total_n_viagens == 0 else random.randrange(total_n_viagens)
    total_n_portos_origem = 20

    return render_template(
        'relatorio/geral.html',
        porto=portos[0],
        data_inicio=data_inicio,
        data_termino=data_termino,
        empresas_to_n_viagens=empresas_to_n_viagens,
        tipo_de_carga_to_cor=tipo_de_carga_to_cor,
        empresas_to_tipo_de_carga=empresas_to_tipo_de_carga,
        tipo_de_carga_to_qty=tipo_de_carga_to_qty,
        total_n_viagens=total_n_viagens,
        total_n_navios=total_n_navios,
        total_n_portos_origem=total_n_portos_origem
    )


@relatorio.route('/gerar/especifico', methods=['POST'])
def gerar_relatorio_especifico(data_inicio, data_termino, id_empresa):
    empresa = empresas[id_empresa - 1]
    navios_da_empresa = [navio for navio in navios if navio['empresa']['id'] == id_empresa]

    navio_to_n_viagens = {
        navio['nome']: random.randrange(80)
        for navio in navios_da_empresa
    }

    tipo_de_carga_to_cor = {
        'Contêiner': '#66c2a5',
        'Reefer': '#8da0cb',
        'Granel': '#fc8d62',
    }

    navio_to_tipo_de_carga = {
        navio['nome']: {
            'Contêiner': random.randrange(80),
            'Reefer': random.randrange(80),
            'Granel': random.randrange(80)
        }
        for navio in navios_da_empresa
    }

    tipo_de_carga_to_qty = {
        tipo: random.randrange(80)
        for tipo in tipo_de_carga_to_cor.keys()
    }

    total_n_viagens = sum(navio_to_n_viagens.values())
    total_n_navios = 0 if total_n_viagens == 0 else random.randrange(total_n_viagens)
    total_n_portos_origem = 20

    return render_template(
        'relatorio/especifico.html',
        porto=portos[0],
        empresa=empresa,
        data_inicio=data_inicio,
        data_termino=data_termino,
        navio_to_n_viagens=navio_to_n_viagens,
        tipo_de_carga_to_cor=tipo_de_carga_to_cor,
        navio_to_tipo_de_carga=navio_to_tipo_de_carga,
        tipo_de_carga_to_qty=tipo_de_carga_to_qty,
        total_n_viagens=total_n_viagens,
        total_n_navios=total_n_navios,
        total_n_portos_origem=total_n_portos_origem
    )
