from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Consultor
from .models import AvatarConfig
from .models import Actividad
from .models import Bonus
from .models import CalculoTotales

##################################
# Autor: Mauricio Olivan Ledezma #
##################################

# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def taskBoard(request):
    consultorList = Consultor.objects.all().values()
    template = loader.get_template("taskBoard.html")
    context  = { 
        "consultorList": consultorList 
    }
    return HttpResponse(template.render(context, request))


def taskBoardForm(request):
    consultorList = Consultor.objects.all().values()
    template = loader.get_template("adminTaskList.html")
    context  = { 
        "consultorList": consultorList 
    }
    return HttpResponse(template.render(context, request))


def manyTaskBoardForm(request):
    consultorList = Consultor.objects.all().values()
    template = loader.get_template("manyTaskList.html")
    context  = { 
        "consultorList": consultorList 
    }
    return HttpResponse(template.render(context, request))


def profile(request):
    template = loader.get_template("profile.html")
    idConsultor = 4
    nombreConsultor = "Marisol Fuentes Díaz"
    cualidades = "*"
    nombreFoto = "AvatarGral.png"
    colorFondo = "01"
    avatar = AvatarConfig.objects.filter(id_consultor=idConsultor).values()
    if (avatar != None) and (avatar):
            cualidades = avatar[0]["cualidades"]
            nombreFoto = avatar[0]["nombre_foto"]
            colorFondo = avatar[0]["color_fondo"]

    context = {
        "idConsultor": idConsultor,
        "consultorName": nombreConsultor,
        "cualidades": cualidades,
        "nombreFoto": nombreFoto,
        "colorFondo": colorFondo
    }
    return HttpResponse(template.render(context, request))


# Para peticiones POST de prueba se deshabilito temporalmente la configuracion anti CSRF.
# En ambiente productivo es importante habilitar la proteccion anti CSRF
@csrf_exempt
def storeActivity(request):
    if request.method == "POST":
        act = Actividad()
        act.id_consultor = request.POST.get('idConsultor')
        act.descrip = request.POST.get('descrip')
        act.categoria = request.POST.get('categoria')
        act.proyecto = request.POST.get('proyecto')
        act.valor = request.POST.get('valor')
        act.estatus = request.POST.get('estatus')
        act.notas = request.POST.get('notas')
        act.fecha_asignacion = request.POST.get('fechaAsignacion')
        act.fecha_entrega = request.POST.get('fechaEntrega')
        act.save()
        return JsonResponse({"stored": "true"}, status=200)
    else:
        return JsonResponse({"error": "true"}, status=400)
    

# Para peticiones POST de prueba se deshabilito temporalmente la configuracion anti CSRF.
# En ambiente productivo es importante habilitar la proteccion anti CSRF
@csrf_exempt
def storeActivityBlock(request):
    if request.method == "POST":
        idsConsultoresList = request.POST.get("idsConsultores")
        idsList = str(idsConsultoresList).split(",")
        descrip   = request.POST.get("descrip")
        categoria = request.POST.get("categoria")
        proyecto  = request.POST.get("proyecto")
        valor     = request.POST.get("valor")
        estatus   = request.POST.get("estatus")
        notas     = request.POST.get("notas")
        fechaAsignacion = request.POST.get("fechaAsignacion")
        fechaEntrega    = request.POST.get("fechaEntrega")

        for idConsultor in idsList:
            if idConsultor == "": 
                continue
            act = Actividad()
            act.id_consultor = idConsultor
            act.descrip = descrip
            act.categoria = categoria
            act.proyecto = proyecto
            act.valor = valor
            act.estatus = estatus
            act.notas = notas
            act.fecha_asignacion = fechaAsignacion
            act.fecha_entrega = fechaEntrega
            act.save()
        return JsonResponse({"stored": "true"}, status=200)
    else:
        return JsonResponse({"error": "true"}, status=400)


def consultTaskList(request):
    if request.method == "GET":
        idConsultor = request.GET.get("idConsultor", None)
        tipoRequest = request.GET.get("tipoRequest", None)
        asignadas  = Actividad.objects.filter(id_consultor=idConsultor, estatus=1)
        enProgreso = Actividad.objects.filter(id_consultor=idConsultor, estatus=2)
        concluidas = Actividad.objects.filter(id_consultor=idConsultor, estatus=3)
        context = {
            "asignadas": asignadas,
            "enProgreso": enProgreso,
            "concluidas": concluidas,
            "tipoRequest": tipoRequest
        }
    else: 
        context = {
            "asignadas": None,
            "enProgreso": None,
            "concluidas": None,
            "tipoRequest": "01"
        }
    
    return render(request, "taskList.html", context)


# Para peticiones POST de prueba se deshabilito temporalmente la configuracion anti CSRF.
# En ambiente productivo es importante habilitar la proteccion anti CSRF
@csrf_exempt
def updateStatusAct(request):
    if request.method == "POST":
        idActividad = request.POST.get("idActivity")
        newStatus   = request.POST.get("newStatus")
        Actividad.objects.filter(id=idActividad).update(estatus=newStatus)
        return JsonResponse({"updated": "true"}, status=200)
    else:
        return JsonResponse({"error": "true"}, status=400)


# Para peticiones POST de prueba se deshabilito temporalmente la configuracion anti CSRF.
# En ambiente productivo es importante habilitar la proteccion anti CSRF
@csrf_exempt
def storeBonus(request):
    if request.method == "POST":
        bonus = Bonus()
        bonus.id_consultor = request.POST.get('idConsultor')
        bonus.descrip = request.POST.get('descrip')
        bonus.valor = request.POST.get('valor')
        bonus.fecha_asignacion = request.POST.get('fechaAsignacion')
        bonus.save()
        return JsonResponse({"stored": "true"}, status=200)
    else:
        return JsonResponse({"error": "true"}, status=400)
    

def consultBonusList(request):
    if request.method == "GET":
        idConsultor = request.GET.get("idConsultor", None)
        bonusList = Bonus.objects.filter(id_consultor=idConsultor)
        context = {
            "bonusList": bonusList
        }
    else: 
        context = {
            "bonusList": None
        }
    
    return render(request, "bonusList.html", context)


def advancePanel(request):
    if request.method == "GET":
        # Realiza la limpieza de la tabla de calculos
        idConsultor = request.GET.get("idConsultor")
        nombreFoto  = request.GET.get("nombreFoto")
        calculo = CalculoTotales.objects.filter(id_consultor=idConsultor)
        if calculo == None:
            calculo = CalculoTotales()
            calculo.id_consultor      = idConsultor
            calculo.total_valor_acts  = 0
            calculo.total_valor_bonus = 0
            calculo.total_valor       = 0
            calculo.save()
        else:
            CalculoTotales.objects.filter(id_consultor=idConsultor).update(total_valor_acts=0, total_valor_bonus=0, total_valor=0)
        context = {
            "error": "false",
            "nombreFoto": nombreFoto
        }
    else: 
        context = {
            "error": "true",
            "nombreFoto": nombreFoto
        }
    return render(request, "advancePanel.html", context)


def consultAdvance(request):
    if request.method == "GET":
        idConsultor  = request.GET.get("idConsultor")
        nombreFoto   = request.GET.get("nombreFoto")
        fechaInicial = request.GET.get("fechaInicial")
        fechaFinal   = request.GET.get("fechaFinal")

        # Se hace el calculo actual de los valores obtenidos
        totalPuntosActs  = Actividad.objects.filter(id_consultor=idConsultor, estatus=3, fecha_entrega__gte = fechaInicial, fecha_entrega__lte = fechaFinal).aggregate(Sum("valor"))['valor__sum']
        totalPuntosBonus = Bonus.objects.filter(id_consultor=idConsultor, fecha_asignacion__gte = fechaInicial, fecha_asignacion__lte = fechaFinal).aggregate(Sum("valor"))['valor__sum']

        if totalPuntosActs == None:
            totalPuntosActs = 0

        if totalPuntosBonus == None:
            totalPuntosBonus = 0
        
        totalPuntos = totalPuntosActs + totalPuntosBonus

        # Se obtiene el valor del anterior calculo almacenado en BD
        calculo = CalculoTotales.objects.filter(id_consultor=idConsultor).values()
        savedNewRecord = True
        if (calculo != None) and (calculo):
            totalPuntosActsAnt  = calculo[0]['total_valor_acts']
            totalPuntosBonusAnt = calculo[0]['total_valor_bonus']
            totalPuntosAnt      = calculo[0]['total_valor']
            savedNewRecord = False
        else:
            totalPuntosActsAnt  = 0
            totalPuntosBonusAnt = 0
            totalPuntosAnt      = 0
            calculo = CalculoTotales()
            calculo.id_consultor      = idConsultor
            calculo.total_valor_acts  = totalPuntosActs
            calculo.total_valor_bonus = totalPuntosBonus
            calculo.total_valor       = totalPuntos
            calculo.save()
            savedNewRecord = True

        if totalPuntosAnt == 0:
            valorX = totalPuntos
        else:
            if totalPuntos == 0:
                valorX = 0
            else:
                valorX = totalPuntosAnt + (totalPuntos - totalPuntosAnt)

        context = {
            "nombreFoto": nombreFoto,
            "totalPuntosActs": totalPuntosActs,
            "totalPuntosBonus": totalPuntosBonus,
            "totalPuntos": totalPuntos,
            "totalPuntosActsAnt": totalPuntosActsAnt,
            "totalPuntosBonusAnt": totalPuntosBonusAnt,
            "totalPuntosAnt": totalPuntosAnt,
            "valorX": valorX
        }

        # Actualiza la tabla de calculos con los ultimos valores calculados
        if not savedNewRecord:
            CalculoTotales.objects.filter(id_consultor=idConsultor).update(total_valor_acts=totalPuntosActs, total_valor_bonus=totalPuntosBonus, total_valor=totalPuntos)
    else: 
        context = {
            "error": "true",
            "totalPuntosActs": 0,
            "totalPuntosBonus": 0,
            "totalPuntos": 0,
            "totalPuntosActsAnt": 0,
            "totalPuntosBonusAnt": 0,
            "totalPuntosAnt": 0,
            "valorX": 0
        }
    return render(request, "advanceDetail.html", context)


def statistics(request):
    if request.method == "GET":
        context = { "error": "false" }
    else: 
        context = { "error": "true" }
    return render(request, "statistics.html", context)


def consultGreenActivities(request):
    listActsEnVerde = list()
    if request.method == "GET":
        fechaInicial = request.GET.get("fechaInicial")
        fechaFinal   = request.GET.get("fechaFinal")

        # Se obtienen todos los ids de los consultores
        consultores = Consultor.objects.values()
        
        if (consultores != None) and (consultores):
            for consultor in consultores:
                # Para cada id se obtiene el calculo de sus actividades concluidas
                numActsEnVerde = Actividad.objects.filter(id_consultor=consultor["id"], estatus=3, fecha_entrega__gte = fechaInicial, fecha_entrega__lte = fechaFinal).count()
                listActsEnVerde.append(str(consultor["id"]) + "-" + str(consultor["nombre"]) + "-" + str(numActsEnVerde))

        context = {
            "listActsEnVerde": listActsEnVerde
        }
    return render(request, "greenActivities.html", context)


# Para peticiones POST de prueba se deshabilito temporalmente la configuracion anti CSRF.
# En ambiente productivo es importante habilitar la proteccion anti CSRF
@csrf_exempt
def storeAvatarSettings(request):
    if request.method == "POST":
        idConsultor = request.POST.get("idConsultor")
        cualities   = request.POST.get("cualidades")
        nombreFoto  = request.POST.get("nombreFoto")
        colorFondo  = request.POST.get("colorFondo")

        result = AvatarConfig.objects.filter(id_consultor=idConsultor)
        if (result != None) and (result):
            result.update(cualidades=cualities, nombre_foto=nombreFoto, color_fondo=colorFondo)
        else:
            avatar = AvatarConfig()
            avatar.id_consultor = idConsultor
            avatar.cualidades  = cualities
            avatar.nombre_foto = nombreFoto
            avatar.color_fondo = colorFondo
            avatar.save()
        return JsonResponse({"stored": "true"}, status=200)
    else:
        return JsonResponse({"error": "true"}, status=400)
    
