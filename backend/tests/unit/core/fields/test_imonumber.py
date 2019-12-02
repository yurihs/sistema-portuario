import pytest
from rest_framework.exceptions import ValidationError

from sistema_portuario.core.fields import IMONumberField


def test_imo_valido(mimesis):
    ev_nautilus_imo = "6711883"
    IMONumberField().to_internal_value(ev_nautilus_imo)


def test_imo_invalido(mimesis):
    with pytest.raises(ValidationError):
        IMONumberField().to_internal_value("1111883")
