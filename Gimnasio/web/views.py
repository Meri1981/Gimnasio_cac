from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from web.models import Clase, Inscripcion
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    context = {"gimnasio": "Gimnasio CaC"}
    return render(request, "web/index.html", context)


def registrarse(request):
    contexto = {}
    if request.method == "GET":
        contexto["registrarse_form"] = RegistrarseForm()
    else:  # asumimos que es un POST
        form = RegistrarseForm(request.POST)
        contexto["registrarse_form"] = form
        if form.is_valid():
            messages.success(request, "Se ha registrado con éxito")

            # print(request.POST)
            return redirect("index")
    return render(request, "web/registrarse.html", contexto)


def lista_clases(request):
    # Gestión de clases. Listado con funcionalidad para agregar, modificar y eliminar clases.
    contexto = {
        "clases": Clase.objects.all().values()
    }

    return render(request, "web/clases.html", contexto)


def crud_clase(request, idClase=None):
    contexto = {}
    if request.method == "GET":
        if idClase == None:
            contexto["clase_form"] = ClaseForm()
        else:
            clase = Clase.objects.filter(id=idClase).values()[0]
            contexto["clase_form"] = ClaseForm(
                {
                    "id": int(clase['id']),
                    "nombre": clase['nombre'],
                    "profesor": clase['profesor'],
                    "cupo": int(clase['cupo']),
                    "horario": clase['horarios'],
                }
            )
    else:
        form = ClaseForm(request.POST)
        contexto["clase_form"] = form
        if form.is_valid():
            clase = Clase()
            clase.nombre = form.cleaned_data['nombre']
            clase.profesor = form.cleaned_data['profesor']
            clase.cupo = form.cleaned_data['cupo']
            clase.horarios = form.cleaned_data['horario']
            clase.save()
            messages.success(request, "Se ha creado la clase")

            return redirect("index")

    return render(request, "web/crud_clase.html", contexto)


def lista_socios(request):
    # Gestión de socios. Listado con funcionalidad para agregar, modificar y eliminar socios.
    contexto = {
        "socios": [
            {
                "id": 1,
                "nombre": "Matias Lopez",
                "dni": "28937123",
                "email": "matutelopez@yahoo.com.ar",
                "plan": "Gold",
            },
            {
                "id": 2,
                "nombre": "Lucas Escobar",
                "dni": "33568789",
                "email": "escobarll@gmail.com",
                "plan": "Silver",
            },
            {
                "id": 3,
                "nombre": "Margarita Maitena",
                "dni": "40578657",
                "email": "maggiemaite2001@gmail.com",
                "plan": "Corporativo",
            },
        ]
    }

    return render(request, "web/socios.html", contexto)


def crud_socio(request, idSocio=None):
    contexto = {}
    if request.method == "GET":
        if idSocio == None:
            contexto["socio_form"] = SocioForm()
        else:
            contexto["socio_form"] = SocioForm(
                {
                    "id": 1,
                    "nombre": "Miriam Losada",
                    "dni": "48058444",
                    "email": "miriamlosada@hotmail.com",
                    "plan": "Basico",
                }
            )
    else:
        contexto["socio_form"] = SocioForm(request.POST)

    return render(request, "web/crud_socio.html", contexto)

class InscripcionListView(ListView):
    model = Inscripcion
    template_name = "web/listado_inscripcion.html"

class InscripcionCreateView(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "web/inscripcion_form.html"
    success_url = reverse_lazy("listado_inscripcion")

class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "web/inscripcion_form.html"
    success_url = reverse_lazy("listado_inscripcion")

class InscripcionDeleteView(DeleteView):
    model = Inscripcion
    template_name = "web/inscripcion_confirm_delete.html"
    success_url = reverse_lazy("listado_inscripcion")

