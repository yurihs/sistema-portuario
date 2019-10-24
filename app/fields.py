from pycpfcnpj import cpf, cnpj
from wtforms.fields import Field
from wtforms.widgets import TextInput
from wtforms.widgets.html5 import TelInput
import phonenumbers

from app.utils import formatar_cpf, formatar_cnpj

class CPFField(Field):
    widget = TextInput()

    def _value(self):
        return '' if self.data is None else formatar_cpf(self.data, pontuacao=True)

    def process_formdata(self, valuelist):
        if valuelist and cpf.validate(valuelist[0]):
            self.data = formatar_cpf(valuelist[0], pontuacao=False)
        else:
            self.data = None
            raise ValueError('CPF inválido')


class CNPJField(Field):
    widget = TextInput()

    def _value(self):
        return '' if self.data is None else formatar_cnpj(self.data, pontuacao=True)

    def process_formdata(self, valuelist):
        if valuelist and cnpj.validate(valuelist[0]):
            self.data = formatar_cnpj(valuelist[0], pontuacao=False)
        else:
            self.data = None
            raise ValueError('CNPJ inválido')


class TelefoneField(Field):
    widget = TelInput()

    def _value(self):
        return '' if self.data is None else self.data

    def process_formdata(self, valuelist):
        if valuelist:
            phone = phonenumbers.parse(valuelist[0], 'BR')
            if phonenumbers.is_valid_number(phone):
                self.data = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.NATIONAL)
                return

        self.data = None
        raise ValueError('Telefone inválido')
