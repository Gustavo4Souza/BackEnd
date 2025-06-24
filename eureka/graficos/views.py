from django.http import JsonResponse, Http404
from .models import Empresa

def api_empresas(request):
    cnpj = request.GET.get('cnpj')
    razao_social = request.GET.get('razao_social')
    nome_fantasia = request.GET.get('nome_fantasia')
    porte = request.GET.get('porte')
    municipio = request.GET.get('municipio')
    uf = request.GET.get('uf')
    cnae_principal = request.GET.get('cnae_principal')

    # filtro especial do vale do pinhão
    vale_do_pinhao = request.GET.get('vale do pinhão')

    empresas = Empresa.objects.all()

    if cnpj:
        empresas = empresas.filter(cnpj__iexact=cnpj)
    if razao_social:
        empresas = empresas.filter(razao_social__icontains=razao_social)
    if nome_fantasia:
        empresas = empresas.filter(nome_fantasia__icontains=nome_fantasia)
    if porte:
        empresas = empresas.filter(porte__icontains=porte)
    if cnae_principal:
        empresas = empresas.filter(cnae_principal__icontains=cnae_principal)
    if uf:
        empresas = empresas.filter(uf__iexact=uf)  
    if municipio:
        empresas = empresas.filter(municipio__icontains=municipio)

    # Filtra ignorando maiúsculas/minúsculas
    if vale_do_pinhao and vale_do_pinhao.lower() in ['sim', 'true', '1']:
        empresas = empresas.filter(
            uf__iexact='PR',
            municipio__icontains='Curitiba'
        )

    dados = []
    for empresa in empresas:
        dados.append({
            'cnpj': empresa.cnpj,
            'razao_social': empresa.razao_social,
            'nome_fantasia': empresa.nome_fantasia,
            'abertura': empresa.abertura,
            'situacao_cadastral': empresa.situacao,
            'tipo_unidade': empresa.tipo,
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
        'situacao_cadastral': empresa.situacao,
        'tipo_unidade': empresa.tipo,
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