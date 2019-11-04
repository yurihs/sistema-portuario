from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from sistema_portuario.core import models

UserAdmin.fieldsets += (("Outros dados", {"fields": ("cpf",)}),)


class CargaInline(admin.TabularInline):
    model = models.Carga


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("linha_1", "cidade", "regiao", "pais", "codigo_postal")


class ViagemAdmin(admin.ModelAdmin):
    inlines = [CargaInline]
    list_display = ("codigo", "navio", "porto_origem")


admin.site.register(models.Carga)
admin.site.register(models.Empresa)
admin.site.register(models.Endereco, EnderecoAdmin)
admin.site.register(models.Navio)
admin.site.register(models.Porto)
admin.site.register(models.TipoCarga)
admin.site.register(models.Usuario, UserAdmin)
admin.site.register(models.Viagem, ViagemAdmin)
