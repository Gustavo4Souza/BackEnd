from django.http import JsonResponse, Http404
from .models import Empresa

def api_empresas(request):
    empresas = Empresa.objects.all()

    dados = []
    for empresa in empresas:
        dados.append({
            'cnpj': empresa.cnpj,
            'razao_social': empresa.razao_social,
            'nome_fantasia': empresa.nome_fantasia,
            'abertura': empresa.abertura,
            'situacao': empresa.situacao,
            'tipo': empresa.tipo,
            'porte': empresa.porte,
            'telefone': empresa.telefone,
            'email': empresa.email,
            'logradouro': empresa.logradouro,
            'numero': empresa.numero,
            'bairro': empresa.bairro,
            'municipio': empresa.municipio,
            'uf': empresa.uf,
            'cep': empresa.cep,
            'cnae_principal': empresa.cnae_principal,
            'cnae_principal_desc': empresa.cnae_principal_desc,
            'cnaes_secundarios': empresa.cnaes_secundarios,
            'socios': empresa.socios,
        })

    return JsonResponse(dados, safe=False)

def api_detalhes_empresa(request, cnpj):
    try:
        empresa = Empresa.objects.get(cnpj=cnpj)
    except Empresa.DoesNotExist:
        raise Http404("Empresa não encontrada")

    dados = {
        'cnpj': empresa.cnpj,
        'razao_social': empresa.razao_social,
        'nome_fantasia': empresa.nome_fantasia,
        'abertura': empresa.abertura,
        'situacao': empresa.situacao,
        'tipo': empresa.tipo,
        'porte': empresa.porte,
        'telefone': empresa.telefone,
        'email': empresa.email,
        'logradouro': empresa.logradouro,
        'numero': empresa.numero,
        'bairro': empresa.bairro,
        'municipio': empresa.municipio,
        'uf': empresa.uf,
        'cep': empresa.cep,
        'cnae_principal': empresa.cnae_principal,
        'cnae_principal_desc': empresa.cnae_principal_desc,
        'cnaes_secundarios': empresa.cnaes_secundarios,
        'socios': empresa.socios,
    }

    return JsonResponse(dados)