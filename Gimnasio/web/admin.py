from django.contrib import admin
from .models import Socio, Clase, Inscripcion, Profesor

class Mi_AdminSite(admin.AdminSite):
    site_header = "Gimnasio CaC"
    site_title = "Administración Gimnasio"
    index_title = "Administrador del sitio"
    empty_value_display = 'No hay registros'

mi_adminsite = Mi_AdminSite(name='myadmin')

mi_adminsite.register(Socio)
mi_adminsite.register(Profesor)
mi_adminsite.register(Clase)
mi_adminsite.register(Inscripcion)