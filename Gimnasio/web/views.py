from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from web.models import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


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

@login_required
def lista_clases(request):
    # Gestión de clases. Listado con funcionalidad para agregar, modificar y eliminar clases.
    contexto = {"clases": Clase.objects.all().values()}

    return render(request, "web/clases.html", contexto)


@permission_required('web.add_clase')
def crud_clase(request, idClase=None, eliminar=None):
    contexto = {}
    if eliminar:
        clase = Clase.objects.get(id=idClase)
        clase.delete()
        messages.success(request, "Se ha eliminado la Clase")

        return redirect("clases")

    if request.method == "GET":
        if idClase == None:
            contexto["clase_form"] = ClaseForm()
        else:
            clase = Clase.objects.filter(id=idClase).values()[0]
            contexto["clase_form"] = ClaseForm(
                {
                    "id": int(clase["id"]),
                    "nombre": clase["nombre"],
                    "profesor": clase["profesor"],
                    "cupo": int(clase["cupo"]),
                    "horario": clase["horarios"],
                }
            )
    else:
        form = ClaseForm(request.POST)
        contexto["clase_form"] = form
        if form.is_valid():
            # Si tiene un ID, es una actualización.
            if form.cleaned_data["id"] != None:
                clase = Clase.objects.get(id=form.cleaned_data["id"])
                mensaje = "Se ha actualizado la clase"
            else:
                clase = Clase()
                mensaje = "Se ha creado la clase"
            clase.nombre = form.cleaned_data["nombre"]
            clase.profesor = form.cleaned_data["profesor"]
            clase.cupo = form.cleaned_data["cupo"]
            clase.horarios = form.cleaned_data["horario"]
            clase.save()
            messages.success(request, mensaje)

            return redirect("clases")

    return render(request, "web/crud_clase.html", contexto)

@login_required
def lista_socios(request):
    contexto = {"socios": Socio.objects.all().values()}

    return render(request, "web/socios.html", contexto)


@login_required(login_url='/accounts/login/') 
@permission_required('web.add_socio',login_url='/accounts/login/', raise_exception=True)
@permission_required('web.change_socio', raise_exception=True)
@permission_required('web.delete_socio', raise_exception=True)
def crud_socio(request, idSocio=None, eliminar=None):

    contexto = {}

    if idSocio:
        try:
            socio = Socio.objects.get(id=idSocio)
        except Socio.DoesNotExist:
            return redirect("socios")

        if eliminar:
            socio = Socio.objects.get(id=idSocio)
            socio.delete()
            messages.success(request, "Se ha eliminado el Socio")
            return redirect("socios")
    else:
        socio = None

    if request.method == "GET":
        if idSocio == None:
            contexto["socio_form"] = SocioForm()
        else:
            socio = Socio.objects.filter(id=idSocio).values()[0]
            contexto["socio_form"] = SocioForm(
                {
                    "id": int(socio["id"]),
                    "nombre": socio["nombre"],
                    "dni": socio["dni"],
                    "email": socio["email"],
                    "plan": socio["plan"],
                }
            )
    else:
        form = SocioForm(request.POST)
        contexto["socio_form"] = form
        if form.is_valid():
            if form.cleaned_data["id"] != None:
                socio = Socio.objects.get(id=form.cleaned_data["id"])
                mensaje = "Se ha actualizado el socio"
            else:
                socio = Socio()
                mensaje = "Se ha creado el socio"

            socio.nombre = form.cleaned_data["nombre"]
            socio.dni = form.cleaned_data["dni"]
            socio.email = form.cleaned_data["email"]
            socio.plan = form.cleaned_data["plan"]
            socio.save()
            messages.success(request, mensaje)

            return redirect("socios")

    return render(request, "web/crud_socio.html", contexto)

@login_required
def lista_profesores(request):
    contexto = {"profesores": Profesor.objects.all().values()}

    return render(request, "web/profesores.html", contexto)

@login_required
def crud_profesor(request, idProfesor=None, eliminar=None):
    contexto = {}

    if idProfesor:
        try:
            profesor = Profesor.objects.get(id=idProfesor)
        except Profesor.DoesNotExist:
            return redirect("profesores")

        if eliminar:
            profesor = Profesor.objects.get(id=idProfesor)
            profesor.delete()
            messages.success(request, "Se ha eliminado el Profesor")
            return redirect("profesores")
    else:
        profesor = None

    if request.method == "GET":
        if idProfesor is None:
            contexto["profesor_form"] = ProfesorForm()
        else:
            profesor = Profesor.objects.filter(id=idProfesor).values()[0]
            contexto["profesor_form"] = ProfesorForm(
                {
                    "id": int(profesor["id"]),
                    "nombre": profesor["nombre"],
                    "dni": profesor["dni"],
                    "email": profesor["email"],
                    "telefono": profesor["telefono"],
                }
            )
    else:
        form = ProfesorForm(request.POST)
        contexto["profesor_form"] = form
        if form.is_valid():
            if form.cleaned_data["id"] != None:
                profesor = Profesor.objects.get(id=form.cleaned_data["id"])
                mensaje = "Se ha actualizado el profesor"
            else:
                profesor = Profesor()
                mensaje = "Se ha creado el profesor"

            profesor.nombre = form.cleaned_data["nombre"]
            profesor.dni = form.cleaned_data["dni"]
            profesor.email = form.cleaned_data["email"]
            profesor.telefono = form.cleaned_data["telefono"]
            profesor.save()
            messages.success(request, mensaje)

            return redirect("profesores")

    contexto["profesor"] = profesor
    return render(request, "web/crud_profesor.html", contexto)


class InscripcionListView(LoginRequiredMixin,ListView):
    model = Inscripcion
    template_name = "web/listado_inscripcion.html"


class InscripcionCreateView(LoginRequiredMixin,CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "web/inscripcion_form.html"
    success_url = reverse_lazy("listado_inscripcion")


class InscripcionUpdateView(LoginRequiredMixin, UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "web/inscripcion_form.html"
    success_url = reverse_lazy("listado_inscripcion")


class InscripcionDeleteView(LoginRequiredMixin, DeleteView):
    model = Inscripcion
    template_name = "web/inscripcion_confirm_delete.html"
    success_url = reverse_lazy("listado_inscripcion")
