from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def familiar_1(request):
    return HttpResponse("este es el primer familiar")


def familiar_2(request):
    return HttpResponse("Este es el segundo familiar")


def fechahoy(request):
    hoy = datetime.now().date()
    return HttpResponse(f"La fecha de hoy es {hoy}")

def vistatemplate(request):
    return render(request, "template.html", context = {}) 

def index(request):
    return render(request, "Inicio/index.html", context={})