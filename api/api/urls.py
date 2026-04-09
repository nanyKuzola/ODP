from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from hospitals.views import indicadores, indicadores_por_uf, indicadores_regiao, indicadores_tempo, top_municipios


def home(request):
    return HttpResponse("ODP Django server running!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path("api/indicadores/", indicadores),
    path("api/indicadores-uf/", indicadores_por_uf),
    path("api/indicadores-regiao/", indicadores_regiao),
    path("api/indicadores-tempo/", indicadores_tempo),
    path("api/top-municipios/", top_municipios),	
]
