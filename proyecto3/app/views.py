from django.shortcuts import render
from .models import *
from .forms import *

def home(request,):
    return render (request,"index.html")

def medicos(request,):
    contexto = {'medicos': medico.objects.all()}
    return render (request,"medicos.html", contexto)

def obra(request,):
    contexto = {'obra': obra_social.objects.all()}
    return render (request,"obra.html", contexto)

def pacientes(request,):
    contexto = {'pacientes': paciente.objects.all()}
    return render (request,"pacientes.html", contexto)

def receta(request,):
    contexto = {'recetas': recetas.objects.all()}
    return render (request,"recetas.html", contexto)

def formularioM (request,):
    if request.method == "POST":
        miformulario = formulariosM(request.POST)    
        if miformulario.is_valid():
            medico_nombre = miformulario.cleaned_data.get("nombre")
            medico_apellido = miformulario.cleaned_data.get("apellido")
            medico_especialización = miformulario.cleaned_data.get("especialización")
            medico_mail = miformulario.cleaned_data.get("mail")
            Medico = medico(nombre=medico_nombre, apellido=medico_apellido, especialización=medico_especialización, mail=medico_mail,)
            Medico.save()
            contexto = {"medicos": medico.objects.all()}
            return render (request, "medicos.html", contexto)
    else:
        miformulario = formulariosM()

    return render (request, "formulariosM.html",{"form":miformulario})

def formularioO (request,):
    if request.method == "POST":
        miformulario = formulariosO(request.POST)    
        if miformulario.is_valid():
            obra_nombre = miformulario.cleaned_data.get("nombre")
            obra_plan = miformulario.cleaned_data.get("plan")
            Obra = obra_social(nombre=obra_nombre, plan=obra_plan,)
            Obra.save()
            contexto = {"obra": obra_social.objects.all()}
            return render (request, "obra.html", contexto)
    else:
        miformulario = formulariosO()

    return render (request, "formulariosO.html",{"form":miformulario})

def formularioP (request,):
    if request.method == "POST":
        miformulario = formulariosP(request.POST)    
        if miformulario.is_valid():
            paciente_nombre = miformulario.cleaned_data.get("nombre")
            paciente_apellido = miformulario.cleaned_data.get("apellido")
            paciente_mail = miformulario.cleaned_data.get("mail")
            Paciente = paciente(nombre=paciente_nombre, apellido=paciente_apellido,  mail=paciente_mail,)
            Paciente.save()
            contexto = {"paciente": paciente.objects.all()}
            return render (request, "pacientes.html", contexto)
    else:
        miformulario = formulariosP()

    return render (request, "formulariosP.html",{"form":miformulario})

def formularioR (request,):
    if request.method == "POST":
        miformulario = formulariosR(request.POST)    
        if miformulario.is_valid():
            
            receta_codigo = miformulario.cleaned_data.get("codigo")
            receta_nombre = miformulario.cleaned_data.get("nombre_del_remedio")
            Receta = recetas(nombre_del_remedio = receta_nombre, codigo=receta_codigo,)
            Receta.save()
            contexto = {"recetas": recetas.objects.all()}
            return render (request, "recetas.html", contexto)
    else:
        miformulario = formulariosR()

    return render (request, "formulariosR.html",{"form":miformulario})


def buscar (request,):
    return render(request,"buscar.html")
def encontrar (request,):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        Medicos = medico.objects.filter(especialización=patron)
        contexto = {"medicos": Medicos}
        return render (request, "medicos.html", contexto)

    contexto = {"medicos": medico.objects.all()}
    return render (request, "medicos.html", contexto)
