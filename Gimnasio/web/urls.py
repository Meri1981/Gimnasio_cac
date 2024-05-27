from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registrarse", views.registrarse, name="registrarse"),
    path("clases", views.lista_clases, name="clases"),
    path("clase", views.crud_clase, name="crud_clase"),
    path("clase/<int:idClase>", views.crud_clase, name="crud_clase"),
    path("socios", views.lista_socios, name="socios"),
    path("socio", views.crud_socio, name="crud_socio"),
    path("socio/<int:idSocio>", views.crud_socio, name="crud_socio"),
]
