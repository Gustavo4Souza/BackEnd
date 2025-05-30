from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensagem": "API de gráficos está no ar!"})

def grafico_faturamento(request):
    dados = {
        "labels": ["Jan", "Fev", "Mar"],
        "data": [10000, 15000, 12000]
    }
    return JsonResponse(dados)

def grafico_clientes(request):
    dados = {
        "labels": ["SP", "RJ", "MG"],
        "data": [40, 25, 35]
    }
    return JsonResponse(dados)
