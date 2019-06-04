import random

from datetime import datetime
from flask import Blueprint, render_template, request

from app.empresa.views import empresas
from app.porto.views import portos

relatorio = Blueprint('relatorio', __name__)


@relatorio.route('/')
def index():
    return render_template('relatorio/index.html', empresas=empresas)


@relatorio.route('/gerar/geral', methods=['POST'])
def gerar_relatorio_geral():
    try:
        data_inicio = datetime.strptime(request.form.get('data_inicio'), '%Y-%m-%d').date()
        data_termino = datetime.strptime(request.form.get('data_termino'), '%Y-%m-%d').date()
    except (ValueError, TypeError) as e:
        return str(e), 400

    empresas_to_n_viagens = {
        empresa['nome_fantasia'] or empresa['razao_social']: random.randrange(80)
        for empresa in empresas
    }

    tipo_de_carga_to_cor = {
        'Contêiner': 'rgb(52, 58, 64)',
        'Reefer': '#007bff'
    }

    empresas_to_tipo_de_carga = {
        empresa['nome_fantasia'] or empresa['razao_social']: {
            'Contêiner': random.randrange(80),
            'Reefer': random.randrange(80)
        }
        for empresa in empresas
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
        total_n_viagens=total_n_viagens,
        total_n_navios=total_n_navios,
        total_n_portos_origem=total_n_portos_origem
    )
