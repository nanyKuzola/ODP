from django.db import models


class IndicadorOncologia(models.Model):

    co_anomes = models.IntegerField()
    co_ibge = models.IntegerField()

    no_municipio = models.CharField(max_length=200)
    sg_uf = models.CharField(max_length=5)
    no_uf = models.CharField(max_length=100)

    co_uf = models.IntegerField()

    co_regiao_brasil = models.IntegerField()
    no_regiao_brasil = models.CharField(max_length=50)
    sg_regiao_brasil = models.CharField(max_length=5)

    co_regiao_saude = models.IntegerField()
    no_regiao_saude = models.CharField(max_length=200)

    co_macro = models.IntegerField()
    no_macro = models.CharField(max_length=200)

    vl_indicador_calculado_mun = models.FloatField()
    vl_indicador_calculado_rs = models.FloatField()
    vl_indicador_calculado_ms = models.FloatField()
    vl_indicador_calculado_uf = models.FloatField()
    vl_indicador_calculado_reg = models.FloatField()
    vl_indicador_calculado_br = models.FloatField()
    vl_indicador_calculado_al = models.FloatField()

    dt_competencia = models.DateTimeField()
    dt_atualizacao = models.DateTimeField()

    ds_unidade_medida = models.CharField(max_length=50)
    sg_granularidade = models.CharField(max_length=10)
    ds_granularidade = models.CharField(max_length=100)

    class Meta:
        db_table = "indicadores_oncologia"

    def __str__(self):
        return f"{self.no_municipio} - {self.co_anomes}"
