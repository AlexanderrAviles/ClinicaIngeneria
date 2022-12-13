from django.contrib import admin
from django.urls import path
from app import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.index, name= "index"),
    path("citas", v.cita, name= "cita"),
    path("pacientes/", v.listarPaciente, name= "lp"),
    path("agregarpaciente/", v.agregarPaciente, name= "ap"),
    path("buscarpaciente/", v.buscarPaciente, name="bcp"),
    path("buscarpaciente/<int:id>", v.modificarPaciente, name="pexp"),
    path("buscarpaciente/<int:id>", v.eliminarPaciente, name="delete"),
]
