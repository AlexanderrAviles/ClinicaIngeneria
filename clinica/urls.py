from django.contrib import admin
from django.urls import path
from app import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.index, name= "index"),
    path("buscarpaciente/", v.buscarPaciente, name="bcp"),
    path("buscarpaciente/expediente/<int:id>", v.expediente, name="pexp"),
]
