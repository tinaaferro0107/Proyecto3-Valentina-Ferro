from django.db import models

# Create your models here.
class obra_social (models.Model):
    nombre = models.CharField(max_length=40)
    plan = models.CharField(max_length=40)
    
class paciente (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField(max_length=100)

class medico (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField(max_length=100)
    especialización = models.CharField(max_length=100)
    
class recetas (models.Model):
    codigo = models.IntegerField()
    nombre_del_remedio = models.CharField(max_length=20)
