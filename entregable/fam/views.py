from django.shortcuts import render
from django.http import HttpResponse
from fam.models import familiar



def creacionfamiliar(request):
    nuevo_fam = familiar.objects.create(nombre = "Juana", edad = 85, parentesco = "Abuela", trabaja = False)
    print(nuevo_fam)
    return HttpResponse("Familiar creado!!! ")


def lista_fam(request):
    all_fam = familiar.objects.all()
    print(all_fam)
    context = {
        "familiares" : all_fam,
    }
    return render(request, "Familiares/lista_fam.html", context = context)

    