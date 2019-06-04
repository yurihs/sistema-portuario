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

    return render_template(
        'relatorio/geral.html',
        porto=portos[0],
        data_inicio=data_inicio,
        data_termino=data_termino
    )
