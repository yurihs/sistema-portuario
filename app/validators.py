from pycpfcnpj import cpfcnpj
from wtforms import ValidationError


class CPF:

    def __call__(self, form, field):
        if not (field.data and cpfcnpj.validate(field.data)):
            raise ValidationError('CPF inválido.')
