from django.urls import path, include
from app.views import *

urlpatterns = [
    path("", home, name= "inicio"),
    path("medicos/", medicos, name= "medicos"),
    path("obras_sociales/", obra, name= "obra_social"),
    path("recetas/", receta, name= "recetas"),
    path("pacientes/", pacientes, name= "pacientes"),

    path("formularioM/", formularioM, name="formularioO"),
    path("formularioP/", formularioP, name="formularioP"),
    path("formularioO/", formularioO, name="formularioO"),
    path("formularioR/", formularioR, name="formularioR"),
    
    path("buscar/",buscar, name="buscar"),
    path("encontrar/",encontrar, name="encontrar"),


]