
from django.http import HttpResponse
from django.template import Template , Context, loader

def saludo(request,nombre):
    return HttpResponse(f"hola {nombre}")

def hola (request, nombre):
    respuesta = f"""
    <html>
    <h1>bienvenido</h1>
    <h2>{nombre}</h2>
    <html> 
    """
    
    return HttpResponse(respuesta)

def hola2 (request):
    a = open ("C:/Users/tinaa/OneDrive/Documents/python/myproject/myproject/plantillas/a.html")
    p = Template(a.read())
    a.close()
    contexto = Context()
    respuesta = p.render(contexto)
    return HttpResponse(respuesta)

def hola3 (request,nombre):
    apellido= "Ferro"
    notas = [8,9,0,6]
    contexto = {"nombre":nombre, "apellidp":apellido, "notas":notas}
    plantilla = loader.get_template("a1.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)


