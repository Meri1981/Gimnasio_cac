from django.urls import path
from . import views
from .views import (
    InscripcionListView,
    InscripcionCreateView,
    InscripcionUpdateView,
    InscripcionDeleteView,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("registrarse", views.registrarse, name="registrarse"),
    path("clases", views.lista_clases, name="clases"),
    path("clase", views.crud_clase, name="crud_clase"),
    path("clase/<int:idClase>", views.crud_clase, name="crud_clase"),
    path("clase/<int:idClase>/<int:eliminar>", views.crud_clase, name="crud_clase"),
    path("socios", views.lista_socios, name="socios"),
    path("socio", views.crud_socio, name="crud_socio"),
    path("socio/<int:idSocio>", views.crud_socio, name="crud_socio"),
    path("socio/<int:idSocio>/<int:eliminar>", views.crud_socio, name="crud_socio"),
    path(
        "listado_inscripcion", InscripcionListView.as_view(), name="listado_inscripcion"
    ),
    path("alta_inscripcion", InscripcionCreateView.as_view(), name="alta_inscripcion"),
    path(
        "<int:pk>/editar_inscripcion",
        InscripcionUpdateView.as_view(),
        name="editar_inscripcion",
    ),
    path(
        "<int:pk>/eliminar_inscripcion/",
        InscripcionDeleteView.as_view(),
        name="eliminar_inscripcion",
    ),
]
