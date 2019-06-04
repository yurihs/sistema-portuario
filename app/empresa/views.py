from flask import Blueprint, render_template

empresa = Blueprint('empresa', __name__)

empresas = [
    dict(
        id=1,
        nome_fantasia='ACME',
        razao_social='ACME Inc.',
        cnpj='06.030.380/0001-93',
        email='contato@acme.example.com',
        telefone='(41) 3752-5161',
        endereco=dict(
            logradouro='Rua Paranavaí, 507',
            cidade='Ariquemes',
            estado='Rondônia',
            pais='Brasil',
            codigo_postal='76876-336'
        )
    ),
    dict(
        id=2,
        nome_fantasia='Maersk Brasil',
        razao_social='Maersk Brasil Brasmar Ltda.',
        cnpj='30.259.220/0001-03',
        email='contato@maersk.example.com',
        telefone='(22) 2974-5741',
        endereco=dict(
            logradouro='Pc Pio X, 79',
            cidade='Rio de Janeiro',
            estado='Rio de Janeiro',
            pais='Brasil',
            codigo_postal='20040-020'
        )
    ),
    dict(
        id=3,
        nome_fantasia='Aliança Navegação',
        razao_social='Aliança Navegação e Logística Ltda.',
        cnpj='03.357.428/0001-84',
        email='sac@alianca.example.com',
        telefone='(92) 3970-3014',
        endereco=dict(
            logradouro='R Des Felismino Soares, 167',
            cidade='Manaus',
            estado='Amazônia',
            pais='Brasil',
            codigo_postal='69070-620'
        )
    ),
    dict(
        id=4,
        nome_fantasia='CMA CGM',
        razao_social='CMA CGM do Brasil Agência Marítima Ltda.',
        cnpj='05.951.386/0003-00',
        email='contact@br.cmacgm.example.com',
        telefone='(97) 3817-8087',
        endereco=dict(
            logradouro='Av Constantino Nery, 2535 Lj 5',
            cidade='Manaus',
            estado='Amazônia',
            pais='Brasil',
            codigo_postal='69050-000'
        )
    )
]


@empresa.route('/')
def listar():
    return render_template('empresa/listar.html', empresas=empresas)


@empresa.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return render_template('empresa/cadastrar.html')


@empresa.route('/<int:id_empresa>')
def editar(id_empresa):
    empresa = empresas[id_empresa-1]
    return render_template('empresa/editar.html', empresa=empresa)
