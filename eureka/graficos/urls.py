from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('faturamento/', views.grafico_faturamento),
    path('clientes/', views.grafico_clientes),
]
