from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Paciente,Prevision,Genero

# Create your views here.


# Menus Recepcionista

def index(request):
    return render(request, "index.html")

def listarPaciente(request):
    paciente = Paciente.objects.all()
    return render(request, "listapacientes.html",{"paciente":paciente})


def buscarPaciente(request):
    buscador = request.GET.get("buscar")
    pacientes = Paciente.objects.filter(rut=buscador)
    print(pacientes)

    return render(request, "buscarpacienterecep.html", {"pacientes": pacientes})

def agregarPaciente(request):
    if request.method == "POST":
        paciente = Paciente()
        paciente.nombre = request.POST["nombre"]
        paciente.apellido_paterno = request.POST["apellidoP"]
        paciente.apellido_materno = request.POST["apellidoM"]
        paciente.rut = request.POST["rut"]
        paciente.fecha_nacimiento = request.POST["fechaNac"]
        paciente.telefono = request.POST["telefono"]
        paciente.direccion = request.POST["direccion"]
        prevision = Prevision.objects.get(id=request.POST["prevision"])
        genero = Genero.objects.get(id=request.POST["genero"])
        paciente.prevision = prevision
        paciente.sexo = genero
        paciente.save()
        return redirect("lp")
    prevision = Prevision.objects.all()
    genero = Genero.objects.all()
    return render(request, "crearPaciente.html",{"genero":genero,"prevision":prevision})


def modificarPaciente(request,id):
    if request.method == 'POST':
        prevision = Prevision.objects.get(id=request.POST["prevision"])
        genero = Genero.objects.get(id=request.POST["genero"])
        paciente = Paciente(id,request.POST["nombre"] ,request.POST["apellidoP"],
                            request.POST["apellidoM"], request.POST["rut"],
                            request.POST["fechaNac"], genero,request.POST["telefono"],
                            request.POST["direccion"],prevision)

        paciente.save()

        return redirect("lp")
    else:
    
        paciente = Paciente.objects.get(id=id)
        genero = Genero.objects.all()
        prevision = Prevision.objects.all()
        return render(request, "modificarPaciente.html", {"paciente":paciente,"genero":genero,"prevision":prevision} )

def eliminarPaciente(request, id):
    paciente = Paciente().objects.get(id=id)
    paciente.delete()

    return redirect("lp")

def cita(request):
    return render(request,"citas.html")

# Menus Kinesiologo


# Menu Admin
