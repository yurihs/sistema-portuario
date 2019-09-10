import pytest

from app.utils import formatar_cpf


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
