from django.http import JsonResponse
from .models import IndicadorOncologia
from django.db.models import Sum

def indicadores(request):

    uf = request.GET.get("uf")
    municipio = request.GET.get("municipio")

    qs = IndicadorOncologia.objects.all()

    if uf:
        qs = qs.filter(sg_uf=uf)

    if municipio:
        qs = qs.filter(no_municipio__icontains=municipio)

    data = list(
        qs.values(
            "no_municipio",
            "sg_uf",
            "vl_indicador_calculado_mun"
        )[:50]
    )

    return JsonResponse(data, safe=False)

def indicadores_por_uf(request):

    data = list(
        IndicadorOncologia.objects
        .values("sg_uf")
        .annotate(total=Sum("vl_indicador_calculado_mun"))
        .order_by("-total")
    )

    return JsonResponse(data, safe=False)




def indicadores_regiao(request):

    data = list(
        IndicadorOncologia.objects
        .values("no_regiao_brasil")
        .annotate(total=Sum("vl_indicador_calculado_mun"))
    )

    return JsonResponse(data, safe=False)



def indicadores_tempo(request):

    data = list(
        IndicadorOncologia.objects
        .values("co_anomes")
        .annotate(total=Sum("vl_indicador_calculado_mun"))
        .order_by("co_anomes")
    )

    return JsonResponse(data, safe=False)



def top_municipios(request):

    data = list(
        IndicadorOncologia.objects
        .values("no_municipio","vl_indicador_calculado_mun")
        .order_by("-vl_indicador_calculado_mun")[:10]
    )

    return JsonResponse(data, safe=False)
