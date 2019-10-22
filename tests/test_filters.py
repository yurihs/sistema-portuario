import pytest

from app.utils import formatar_cpf, formatar_cnpj


def test_formatar_cpf_valido():
	com_pontuacao = '204.475.272-74'
	sem_pontuacao = '20447527274'

	assert formatar_cpf(com_pontuacao, pontuacao=False) == sem_pontuacao
	assert formatar_cpf(com_pontuacao, pontuacao=True) == com_pontuacao
	assert formatar_cpf(sem_pontuacao, pontuacao=False) == sem_pontuacao
	assert formatar_cpf(sem_pontuacao, pontuacao=True) == com_pontuacao


def test_formatar_cpf_invalido():
	com_pontuacao = '123.456.736'
	sem_pontuacao = '123456736'

	with pytest.raises(ValueError):
		formatar_cpf(com_pontuacao, pontuacao=False)

	with pytest.raises(ValueError):
		formatar_cpf(com_pontuacao, pontuacao=True)

	with pytest.raises(ValueError):
		formatar_cpf(sem_pontuacao, pontuacao=False)

	with pytest.raises(ValueError):
		formatar_cpf(sem_pontuacao, pontuacao=True)



def test_formatar_cnpj_valido():
	com_pontuacao = '82.303.908/0001-39'
	sem_pontuacao = '82303908000139'

	assert formatar_cnpj(com_pontuacao, pontuacao=False) == sem_pontuacao
	assert formatar_cnpj(com_pontuacao, pontuacao=True) == com_pontuacao
	assert formatar_cnpj(sem_pontuacao, pontuacao=False) == sem_pontuacao
	assert formatar_cnpj(sem_pontuacao, pontuacao=True) == com_pontuacao


def test_formatar_cnpj_invalido():
	com_pontuacao = '12.345.678/90-34'
	sem_pontuacao = '123456789034'

	with pytest.raises(ValueError):
		formatar_cnpj(com_pontuacao, pontuacao=False)

	with pytest.raises(ValueError):
		formatar_cnpj(com_pontuacao, pontuacao=True)

	with pytest.raises(ValueError):
		formatar_cnpj(sem_pontuacao, pontuacao=False)

	with pytest.raises(ValueError):
		formatar_cnpj(sem_pontuacao, pontuacao=True)
