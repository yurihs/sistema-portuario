from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    cpf = models.CharField("CPF", max_length=255, unique=True)
    email = models.EmailField("E-mail", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "cpf"]


class Endereco(models.Model):
    linha_1 = models.CharField(
        "Linha 1", max_length=255, help_text="Rua, avenida, etc."
    )
    cidade = models.CharField("Cidade", max_length=255)
    regiao = models.CharField(
        "Região", max_length=255, help_text="Estado, província, etc."
    )
    codigo_postal = models.CharField("Código postal", max_length=255)
    pais = models.CharField("País", max_length=255)

    def __str__(self):
        return "{}, {}, {}".format(self.linha_1, self.cidade, self.pais)

    class Meta:
        verbose_name = "endereço"
        verbose_name_plural = "endereços"


class Empresa(models.Model):
    cnpj = models.CharField("CNPJ", max_length=255, unique=True)
    nome_fantasia = models.CharField("Nome fantasia", max_length=255)
    razao_social = models.CharField("Razão social", max_length=255)
    email = models.EmailField("E-mail", blank=True)
    telefone = models.CharField("Telefone", max_length=255, blank=True)

    endereco = models.ForeignKey(
        Endereco, related_name="+", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.nome_fantasia


class TipoCarga(models.Model):
    nome = models.CharField("Nome", max_length=255, unique=True)
    unidade = models.CharField(
        "Símbolo da unidade de medida", max_length=255, help_text="kg, L, m3, etc."
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "tipo de carga"
        verbose_name_plural = "tipos de carga"


class Navio(models.Model):
    numero_imo = models.CharField("Número IMO", max_length=255, unique=True)
    nome = models.CharField("Nome", max_length=255)
    estado_bandeira = models.CharField("Estado de bandeira", max_length=255)
    comprimento_metros = models.PositiveIntegerField(
        "Comprimento em metros", blank=True, null=True
    )
    largura_metros = models.PositiveIntegerField(
        "Largura em metros", blank=True, null=True
    )
    numero_de_tripulantes = models.PositiveIntegerField(
        "Número de tripulantes", blank=True, null=True
    )
    porte_bruto_toneladas = models.PositiveIntegerField(
        "Porte bruto em toneladas", blank=True, null=True
    )

    empresa = models.ForeignKey(
        Empresa, related_name="navios", on_delete=models.PROTECT
    )
    tipos_de_carga_suportados = models.ManyToManyField(
        TipoCarga,
        verbose_name="Tipos de carga suportados",
        related_name="+",
        blank=True,
    )

    def __str__(self):
        return self.nome


class Porto(models.Model):
    un_locode = models.CharField("UN/LOCODE", max_length=255, unique=True)
    nome = models.CharField("Nome", max_length=255)
    capacidade_teus_anuais = models.PositiveIntegerField(
        "Capacidade em TEUs anuais", blank=True, null=True
    )

    endereco = models.ForeignKey(Endereco, related_name="+", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Viagem(models.Model):
    codigo = models.CharField("Código", max_length=255)
    data_chegada = models.DateTimeField("Data de chegada", blank=True, null=True)
    data_atracacao = models.DateTimeField("Data de atracação", blank=True, null=True)
    data_liberacao = models.DateTimeField("Data de liberação", blank=True, null=True)
    data_saida = models.DateTimeField("Data de saída", blank=True, null=True)

    navio = models.ForeignKey(Navio, related_name="viagens", on_delete=models.PROTECT)
    porto_origem = models.ForeignKey(
        Porto,
        verbose_name="Porto de origem",
        related_name="viagens",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "viagem"
        verbose_name_plural = "viagens"


class Carga(models.Model):
    quantidade = models.PositiveIntegerField("Quantidade")

    viagem = models.ForeignKey(Viagem, related_name="cargas", on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoCarga, related_name="+", on_delete=models.PROTECT)

    def __str__(self):
        return "{qtd:d}{unid:s} {nome:s}".format(
            qtd=self.quantidade, unid=self.tipo.unidade, nome=self.tipo.nome
        )
