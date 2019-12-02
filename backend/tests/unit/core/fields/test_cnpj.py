import pytest
from rest_framework.exceptions import ValidationError

from sistema_portuario.core.fields import CNPJField


def test_cnpj_valido_to_internal(mimesis):
    field = CNPJField()

    valido_com_mascara = "55.791.882/0001-42"
    valido_sem_mascara = "55791882000142"

    internal_value = field.to_internal_value(valido_com_mascara)

    assert internal_value == valido_sem_mascara


def test_cnpj_valido_to_representation(mimesis):
    field = CNPJField()

    valido_com_mascara = "55.791.882/0001-42"
    valido_sem_mascara = "55791882000142"

    representation = field.to_representation(valido_sem_mascara)

    assert representation == valido_com_mascara


def test_cnpj_invalido(mimesis):
    field = CNPJField()

    invalido = "11.791.882/0001-11"

    with pytest.raises(ValidationError):
        field.to_internal_value(invalido)
