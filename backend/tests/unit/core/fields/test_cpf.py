import pytest
from rest_framework.exceptions import ValidationError

from sistema_portuario.core.fields import CPFField


def test_cpf_valido_to_internal(mimesis):
    field = CPFField()

    valido_com_mascara = "242.078.580-08"
    valido_sem_mascara = "24207858008"

    internal_value = field.to_internal_value(valido_com_mascara)

    assert internal_value == valido_sem_mascara


def test_cpf_valido_to_representation(mimesis):
    field = CPFField()

    valido_com_mascara = "242.078.580-08"
    valido_sem_mascara = "24207858008"

    representation = field.to_representation(valido_sem_mascara)

    assert representation == valido_com_mascara


def test_cpf_invalido(mimesis):
    field = CPFField()

    invalido = "111.222.580-11"

    with pytest.raises(ValidationError):
        field.to_internal_value(invalido)
