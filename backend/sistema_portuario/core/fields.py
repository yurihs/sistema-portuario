import pycpfcnpj.cnpj
import pycpfcnpj.cpf
from django.contrib.auth.models import Group
from django.db.models import Manager
from rest_framework.fields import CharField, Field
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField

from sistema_portuario.core.utils import validar_imo


class CNPJField(CharField):
    default_error_messages = {"invalid": "CNPJ inválido."}

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if not pycpfcnpj.cnpj.validate(data):
            self.fail("invalid", value=data)

        somente_digitos = "".join(x for x in data if x.isdigit())
        return somente_digitos

    def to_representation(self, value):
        value = super().to_representation(value)
        return "{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}".format(*value)


class CPFField(CharField):
    default_error_messages = {"invalid": "CPF inválido."}

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if not pycpfcnpj.cpf.validate(data):
            self.fail("invalid", value=data)

        somente_digitos = "".join(x for x in data if x.isdigit())
        return somente_digitos

    def to_representation(self, value):
        value = super().to_representation(value)
        return "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*value)


class IMONumberField(CharField):
    default_error_messages = {"invalid": "Número IMO inválido."}

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if not isinstance(data, str):
            self.fail("invalid", value=data)
        if not validar_imo(data):
            self.fail("invalid", value=data)

        return data


class SingleGroupField(Field):
    default_error_messages = {"invalid": "Grupo inválido."}

    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail("invalid", value=data)
        nomes_grupos = Group.objects.order_by("id").values_list("name", flat=True)
        if data not in nomes_grupos:
            self.fail("invalid", value=data)
        return [data]

    def to_representation(self, values):
        if isinstance(values, Manager):
            if values.count() > 0:
                return values.first().name
            elif hasattr(values, "__iter__"):
                for value in values:
                    return value
        return None


class PresentableRelatedFieldMixin:
    def __init__(self, **kwargs):
        self.presentation_serializer_class = kwargs.pop(
            "presentation_serializer_class", None
        )
        assert (
            self.presentation_serializer_class is not None
        ), "The `presentation_serializer_class` argument is required"
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, data):
        return self.presentation_serializer_class(data, context=self.context).data


class PresentablePrimaryKeyRelatedField(
    PresentableRelatedFieldMixin, PrimaryKeyRelatedField
):
    pass


class PresentableSlugRelatedField(PresentableRelatedFieldMixin, SlugRelatedField):
    pass
