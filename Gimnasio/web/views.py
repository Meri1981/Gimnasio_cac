from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
         "gimnasio" : "Gimnasio CaC" }
    return render(request, "web/index.html", context)



def registrarse(request):
    contexto ={}
    if request.method == 'GET':
            contexto['registrarse_form'] = RegistrarseForm()
    else: #asumimos que es un POST
        form = RegistrarseForm(request.POST)
        contexto['registrarse_form'] = form
        if form.is_valid():
            messages.success(request, "Se ha registrado con éxito")

        #print(request.POST)
            return redirect('index')
    return render(request, 'web/registrarse.html', contexto)

def lista_clases(request):
     #Gestión de clases. Listado con funcionalidad para agregar, modificar y eliminar clases.
     contexto = {"clases":[
          {"id": 1, "nombre": "Cross fit", "profesor": "Juan Pérez", "cupo": 12, "horario": "LU-MI-VI 20hs."},
          {"id": 2, "nombre": "Pilates", "profesor": "Matilde Pilate", "cupo": 10, "horario": "LU-MI-VI 10hs."},
          {"id": 3, "nombre": "Spinning", "profesor": "Ramón Valdez", "cupo": 20, "horario": "MA-JU 19hs."}
          ]}
     
     return render(request, 'web/clases.html', contexto)

def crud_clase(request, idClase = None):
    contexto = {}
    if request.method == 'GET':
        if idClase == None:
            contexto['clase_form'] = ClaseForm()
        else:
            contexto['clase_form'] = ClaseForm({"id": 1, "nombre": "Cross fit", "profesor": "Juan Pérez", "cupo": 12, "horario": "LU-MI-VI 20hs."})
    else:
        contexto['clase_form'] = ClaseForm(request.POST)
    
    return render(request, 'web/crud_clase.html', contexto)
