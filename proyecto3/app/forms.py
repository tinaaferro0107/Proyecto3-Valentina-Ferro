from django import forms

class formulariosM (forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    mail = forms.EmailField(max_length=100, required=True)
    especialización = forms.CharField(max_length=100, required=True)

class formulariosP (forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    mail = forms.EmailField(max_length=100, required=True)

class formulariosO (forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    plan = forms.CharField(max_length=40, required=True)
    
class formulariosR (forms.Form):
    codigo = forms.IntegerField()
    nombre_del_remedio = forms.CharField(max_length=20, required=True)