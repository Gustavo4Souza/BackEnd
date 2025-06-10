from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(max_length=20, primary_key=True)
    razao_social = models.CharField(max_length=255, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    abertura = models.DateField(null=True, blank=True)
    situacao = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    porte = models.CharField(max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    cnae_principal = models.CharField(max_length=20, null=True, blank=True)
    cnae_principal_desc = models.CharField(max_length=255, null=True, blank=True)
    cnaes_secundarios = models.TextField(null=True, blank=True)
    socios = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'CNAE'  # corresponde ao nome da tabela MySQL
        managed = False  # importante para evitar que o Django tente criar ou alterar a tabela no banco de dados

    def __str__(self):
        return f"{self.razao_social or self.nome_fantasia or self.cnpj}"
