import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

from hospitals.models import IndicadorOncologia

# caminho do JSON
json_file = "/var/www/cane_regnet/ODP/data/raw/ccmhhcac.json"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:

    IndicadorOncologia.objects.create(
        co_anomes=item.get("co_anomes"),
        co_ibge=item.get("co_ibge"),
        no_municipio=item.get("no_municipio"),
        sg_uf=item.get("sg_uf"),
        no_uf=item.get("no_uf"),
        co_uf=item.get("co_uf"),
        co_regiao_brasil=item.get("co_regiao_brasil"),
        no_regiao_brasil=item.get("no_regiao_brasil"),
        sg_regiao_brasil=item.get("sg_regiao_brasil"),
        co_regiao_saude=item.get("co_regiao_saude"),
        no_regiao_saude=item.get("no_regiao_saude"),
        co_macro=item.get("co_macro"),
        no_macro=item.get("no_macro"),
        vl_indicador_calculado_mun=item.get("vl_indicador_calculado_mun"),
        vl_indicador_calculado_rs=item.get("vl_indicador_calculado_rs"),
        vl_indicador_calculado_ms=item.get("vl_indicador_calculado_ms"),
        vl_indicador_calculado_uf=item.get("vl_indicador_calculado_uf"),
        vl_indicador_calculado_reg=item.get("vl_indicador_calculado_reg"),
        vl_indicador_calculado_br=item.get("vl_indicador_calculado_br"),
        vl_indicador_calculado_al=item.get("vl_indicador_calculado_al"),
        dt_competencia=item.get("dt_competencia"),
        dt_atualizacao=item.get("dt_atualizacao"),
        ds_unidade_medida=item.get("ds_unidade_medida"),
        sg_granularidade=item.get("sg_granularidade"),
        ds_granularidade=item.get("ds_granularidade"),
    )

print("Importação concluída")
