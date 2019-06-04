from flask import Blueprint, render_template

from app.empresa.views import empresas

relatorio = Blueprint('relatorio', __name__)

@relatorio.route('/')
def index():
    return render_template('relatorio/index.html', empresas=empresas)
