from django.shortcuts import render
from django.db.models import Q
from .models import Paciente

# Create your views here.


# Menus Recepcionista

def index(request):
    return render(request, "index.html")


def buscarPaciente(request):
    buscador = request.GET.get("buscar")
    pacientes = Paciente.objects.filter(rut=buscador)
    print(pacientes)

    return render(request, "buscarpacienterecep.html", {"pacientes": pacientes})


def expediente(request,id):
    paciente = Paciente.objects.get(id=id)
    return render(request, "expediente.html", {"paciente":paciente} )

# Menus Kinesiologo


# Menu Admin
