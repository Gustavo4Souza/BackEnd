from django.contrib import admin
from django.urls import path, include
from graficos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # tudo de gráfico passa por aqui
    path('api/graficos/', include('graficos.urls')),  
]
