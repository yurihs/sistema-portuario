from pycpfcnpj import cpfcnpj
from wtforms.fields import Field
from wtforms.widgets import TextInput

from app.utils import formatar_cpf

class CPFField(Field):
    widget = TextInput()

    def _value(self):
        return '' if self.data is None else formatar_cpf(self.data, pontuacao=True)

    def process_formdata(self, valuelist):
        if valuelist and cpfcnpj.validate(valuelist[0]):
            self.data = formatar_cpf(valuelist[0], pontuacao=False)
        else:
            self.data = None
            raise ValueError('CPF inválido')
