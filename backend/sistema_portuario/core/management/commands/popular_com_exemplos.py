import random
import string
import unicodedata
from datetime import timedelta

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from mimesis import Generic
from mimesis.builtins import BrazilSpecProvider
from yaspin import yaspin
from yaspin.spinners import Spinners

from sistema_portuario import settings
from sistema_portuario.core import models
from sistema_portuario.core.utils import gerar_numero_imo

gen = Generic("pt-br")
BrazilSpecProvider.Meta.name = "brasil"
gen.add_provider(BrazilSpecProvider)
locales = ["pt-br", "en", "es", "nl", "de"]


class Command(BaseCommand):
    help = "Popula o banco de dados com dados de exemplo"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spinner = yaspin(Spinners.dots4)

    def set_status(self, text, *args, **kwargs):
        self.spinner.text = text.format(*args, **kwargs)

    def write_success(self, message):
        self.spinner.write("{} {}".format(self.style.SUCCESS("✓"), message))

    def handle(self, *args, **options):
        self.spinner.start()
        self.spinner.write("Populando o banco de dados com dados de exemplo...")

        self.popular_tudo()

        self.spinner.stop()

    def popular_tudo(self):
        self.popular_usuarios()
        self.popular_empresas()
        self.popular_navios(empresas=models.Empresa.objects.all())
        self.popular_tipos_carga()
        self.popular_tipos_carga_suportados(
            navios=models.Navio.objects.all(),
            tipos_carga=models.TipoCarga.objects.all(),
        )
        self.popular_portos()
        self.popular_viagens(
            navios=models.Navio.objects.all(), portos=models.Porto.objects.all()
        )
        self.popular_cargas_viagens(navios=models.Navio.objects.all())

    def popular_usuarios(self, n_funcionarios=7, n_administradores=2):
        self.set_status("Populando {} usuários", n_funcionarios + n_administradores)
        grupo_administradores = Group.objects.get(name="Administradores")
        grupo_funcionarios = Group.objects.get(name="Funcionários")

        for _ in range(n_funcionarios):
            funcionario = self.gerar_usuario()
            funcionario.save()
            funcionario.groups.add(grupo_funcionarios)

        for _ in range(n_administradores):
            administrador = self.gerar_usuario()
            administrador.save()
            administrador.groups.add(grupo_administradores)

        self.write_success("Usuários")

    def popular_empresas(self, n_empresas=40):
        self.set_status("Populando {} empresas", n_empresas)
        for _ in range(n_empresas):
            empresa = self.gerar_empresa()
            if empresa.endereco is not None:
                empresa.endereco.save()
                empresa.endereco = empresa.endereco
            empresa.save()
        self.write_success("Empresas")

    def popular_navios(self, empresas, max_navios_por_empresa=10):
        imos = set()
        n_empresas = empresas.count()
        n_digitos_empresas = len(str(n_empresas))
        for i, empresa in enumerate(empresas, start=1):
            self.set_status(
                "Populando navios: [{}/{} empresas] {}",
                str(i).rjust(n_digitos_empresas),
                n_empresas,
                empresa,
            )
            navios = []
            for _ in range(gen.numbers.between(0, max_navios_por_empresa)):
                navio = self.gerar_navio(empresa)
                if navio.numero_imo in imos:
                    continue
                navios.append(navio)
                imos.add(navio.numero_imo)
            models.Navio.objects.bulk_create(navios)
        self.write_success("Navios")

    def popular_tipos_carga(self, n_tipos=30):
        self.set_status("Populando {} tipos de carga", n_tipos)
        nome_to_tipo = {}
        n_tipos_gerados = 0
        while n_tipos_gerados < n_tipos:
            tipo = self.gerar_tipo_carga()
            if tipo.nome not in nome_to_tipo:
                nome_to_tipo[tipo.nome] = tipo
                n_tipos_gerados += 1
        models.TipoCarga.objects.bulk_create(nome_to_tipo.values())
        self.write_success("Tipos de carga")

    def popular_tipos_carga_suportados(
        self, navios, tipos_carga, max_tipos_por_navio=10
    ):
        tipos_carga = list(tipos_carga)
        n_navios = navios.count()
        n_digitos_navios = len(str(n_navios))
        for i, navio in enumerate(navios, start=1):
            self.set_status(
                "Populando tipos de carga suportados: [{}/{} navios] {}",
                str(i).rjust(n_digitos_navios),
                n_navios,
                navio,
            )
            navio_tipos_suportados = random.choices(
                tipos_carga, k=gen.numbers.between(0, max_tipos_por_navio)
            )
            if navio_tipos_suportados:
                navio.tipos_de_carga_suportados.add(*navio_tipos_suportados)
        self.write_success("Tipos de carga suportados pelos navios")

    def popular_portos(self, n_portos=100):
        self.set_status("Populando portos")
        n_digitos_portos = len(str(n_portos))

        un_locodes = set()
        n_portos_criados = 0
        while n_portos_criados < n_portos:
            porto = self.gerar_porto()
            if porto.un_locode in un_locodes:
                continue
            un_locodes.add(porto.un_locode)
            porto.endereco.save()
            porto.endereco = porto.endereco
            porto.save()
            n_portos_criados += 1
            self.set_status(
                "Populando portos [{}/{}]",
                str(n_portos_criados).rjust(n_digitos_portos),
                n_portos,
            )
        self.write_success("Portos")

    def popular_viagens(self, navios, portos, max_viagens_por_navio=10):
        self.set_status("Populando viagens")
        portos = list(portos)
        n_navios = navios.count()
        n_digitos_navios = len(str(n_navios))
        for i, navio in enumerate(navios, start=1):
            self.set_status(
                "Populando viagens: [{}/{} navios] {}",
                str(i).rjust(n_digitos_navios),
                n_navios,
                navio,
            )
            for _ in range(gen.numbers.between(0, max_viagens_por_navio)):
                porto = random.choice(portos)
                viagem = self.gerar_viagem(navio=navio, porto=porto)
                viagem.save()
        self.write_success("Viagens")

    def popular_cargas_viagens(self, navios):
        self.set_status("Populando cargas")
        n_navios = navios.count()
        n_digitos_navios = len(str(n_navios))
        for i, navio in enumerate(navios, start=1):
            tipos_suportados = list(navio.tipos_de_carga_suportados.all())
            n_tipos_suportados = len(tipos_suportados)
            if n_tipos_suportados == 0:
                continue

            for viagem in navio.viagens.all():
                self.set_status(
                    "Populando cargas: [{}/{} navios] {} (navio {})",
                    str(i).rjust(n_digitos_navios),
                    n_navios,
                    viagem,
                    navio,
                )
                tipos_selecionados = random.sample(
                    tipos_suportados, k=gen.numbers.between(1, n_tipos_suportados)
                )
                for tipo in tipos_selecionados:
                    carga = self.gerar_carga(viagem=viagem, tipo=tipo)
                    carga.save()
                    viagem.cargas.add(carga)
        self.write_success("Cargas")

    def talvez_gerar(self, func, frequencia=0.5):
        if random.random() <= frequencia:
            return func()
        return None

    def gerar_usuario(self):
        email = gen.person.email(["@example.com"])
        usuario = models.Usuario(
            email=email, username=email, cpf=gen.brasil.cpf(with_mask=False)
        )
        usuario.set_password("123")
        return usuario

    def gerar_empresa(self):
        nome_fantasia = gen.business.company()
        razao_social = "{} {}".format(nome_fantasia, gen.business.company_type())

        empresa = models.Empresa(
            cnpj=gen.brasil.cnpj(with_mask=False),
            nome_fantasia=nome_fantasia,
            razao_social=razao_social,
            email=self.talvez_gerar(gen.person.email) or "",
            telefone=self.talvez_gerar(gen.person.telephone) or "",
            endereco=self.talvez_gerar(self.gerar_endereco),
        )
        return empresa

    def gerar_endereco(self, locale="pt-br"):
        with gen.address.override_locale(locale):
            return models.Endereco(
                linha_1=gen.address.address(),
                cidade=gen.address.city(),
                regiao=gen.address.state(),
                pais=gen.address.country(),
                codigo_postal=gen.address.postal_code(),
            )

    def gerar_tipo_carga(self):
        geradores = (
            gen.food.drink,
            gen.food.fruit,
            gen.food.vegetable,
            gen.science.chemical_element,
        )

        return models.TipoCarga(
            nome=random.choice(geradores)(), unidade=gen.unit_system.unit(symbol=True)
        )

    def gerar_navio(self, empresa):
        geradores_nome = (
            lambda: "{} {}".format(gen.person.name(), gen.hardware.cpu_codename()),
            lambda: "{} {}".format(gen.person.last_name(), gen.text.color()),
            lambda: "SÃO {}".format(gen.person.name()).upper(),
            gen.address.street_name,
        )

        return models.Navio(
            numero_imo=gerar_numero_imo(),
            nome=random.choice(geradores_nome)(),
            estado_bandeira=gen.address.country_code(),
            comprimento_metros=self.talvez_gerar(lambda: gen.numbers.between(200, 500)),
            largura_metros=self.talvez_gerar(lambda: gen.numbers.between(20, 60)),
            numero_de_tripulantes=self.talvez_gerar(
                lambda: gen.numbers.between(10, 60)
            ),
            porte_bruto_toneladas=self.talvez_gerar(
                lambda: gen.numbers.between(30, 700000)
            ),
            empresa=empresa,
        )

    def gerar_porto(self):
        locale = random.choice(locales)
        with gen.address.override_locale(locale):
            nome = gen.address.city()
        return models.Porto(
            un_locode=self.gerar_un_locode(locale),
            nome=nome,
            capacidade_teus_anuais=self.talvez_gerar(
                lambda: gen.numbers.between(1000, 5000000)
            ),
            endereco=self.gerar_endereco(locale=locale),
        )

    def gerar_un_locode(self, locale=None):
        if locale is None:
            sigla_pais = gen.address.country_code()
        else:
            sigla_pais = locale[-2:].upper()

        codigo = "".join(random.choices(string.ascii_uppercase, k=3))
        return sigla_pais + codigo

    def gerar_viagem(self, navio, porto):
        data_chegada = gen.datetime.datetime(timezone=settings.TIME_ZONE)
        data_atracacao = data_chegada + self.gerar_atraso()
        data_liberacao = data_atracacao + self.gerar_atraso()
        data_saida = data_liberacao + self.gerar_atraso()
        return models.Viagem(
            codigo=self.gerar_codigo_viagem(nome_navio=navio.nome),
            data_chegada=data_chegada,
            data_atracacao=data_atracacao,
            data_liberacao=data_liberacao,
            data_saida=data_saida,
            navio=navio,
            porto_origem=porto,
        )

    def gerar_atraso(self):
        return timedelta(
            days=gen.numbers.between(0, 2),
            hours=gen.numbers.between(0, 6),
            minutes=gen.numbers.between(0, 59),
            seconds=gen.numbers.between(0, 59),
        )

    def remover_acentos(self, s):
        return "".join(
            c
            for c in unicodedata.normalize("NFD", s)
            if unicodedata.category(c) != "Mn"
        )

    def gerar_codigo_viagem(self, nome_navio):
        return "{:.6s}{:05d}".format(
            self.remover_acentos(nome_navio.upper().replace(" ", "")),
            gen.numbers.between(0, 100000 - 1),
        )

    def gerar_carga(self, viagem, tipo):
        return models.Carga(
            viagem=viagem, tipo=tipo, quantidade=gen.numbers.between(1, 1000000)
        )
