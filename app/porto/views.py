from flask import Blueprint, render_template

porto = Blueprint('porto', __name__)

portos = [
    dict(
        id=1,
        nome='Porto de Salvador',
        endereco=dict(
            logradouro='Av. França, 1551 I',
            cidade='Salvador',
            estado='Bahia',
            pais='Brasil',
            codigo_postal='40010-000',
        ),
        capacidade_teus_anuais=300_000,
        un_locode='BRSSA',
    ),
    dict(
        id=2,
        nome='Porto de Itaguaí',
        endereco=dict(
            logradouro='Estrada Prefeito Wilson Pedro Francisco, s/n',
            cidade='Itaguaí',
            estado='Rio de Janeiro',
            pais='Brasil',
            codigo_postal='23825-410',
        ),
        capacidade_teus_anuais=250_000,
        un_locode='BRIGI',
    ),
    dict(
        id=3,
        nome='Porto de Barra do Riacho',
        endereco=dict(
            logradouro='Caminho da Barra do Riacho, s/n',
            cidade='Aracruz',
            estado='Espírito Santo',
            pais='Brasil',
            codigo_postal='29197-000',
        ),
        capacidade_teus_anuais=40_000,
        un_locode='BRRCH',
    ),
    dict(
        id=4,
        nome='Porto de Itapoá',
        endereco=dict(
            logradouro='Avenida Beira Mar 05, 2900',
            cidade='Itapoá',
            estado='Santa Catarina',
            pais='Brasil',
            codigo_postal='89249-000',
        ),
        capacidade_teus_anuais=1_200_000,
        un_locode='BRIOA',
    ),
    dict(
        id=5,
        nome='Porto de Singapura',
        endereco=dict(
            logradouro='Rua Alexandra, 460',
            pais='Singapura',
            codigo_postal='119963',
        ),
        capacidade_teus_anuais=32_200_000,
        un_locode='SGSIN',
    )
]


@porto.route('/')
def listar():
    return render_template('porto/listar.html', portos=portos)


@porto.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return render_template('porto/cadastrar.html')


@porto.route('/<int:id_porto>')
def editar(id_porto):
    porto = portos[id_porto-1]
    return render_template('porto/editar.html', porto=porto)
