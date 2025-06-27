from django.urls import path
from . import views

urlpatterns = [
    path('api/empresas/', views.api_empresas, name='api_empresas'),
    path('api/empresas/<path:cnpj>/', views.api_detalhes_empresa, name='api_detalhes_empresa'),
]
