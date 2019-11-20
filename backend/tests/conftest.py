import pytest
from django.core.management import call_command
from mimesis.builtins import BrazilSpecProvider
from mimesis.schema import Field


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "essencial.json")


@pytest.fixture()
def mimesis():
    BrazilSpecProvider.Meta.name = "brasil"
    return Field("en", providers=[BrazilSpecProvider])
