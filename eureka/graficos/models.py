from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(max_length=18, primary_key=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    abertura = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    porte = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=20, blank=True, null=True)
    cnae_principal = models.CharField(max_length=20, blank=True, null=True)
    cnae_principal_desc = models.CharField(max_length=255, blank=True, null=True)
    cnaes_secundarios = models.TextField(blank=True, null=True)
    socios = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cnae'
