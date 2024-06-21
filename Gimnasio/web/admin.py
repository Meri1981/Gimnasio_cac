

from django.contrib import admin
from .models import Socio, Profesor, Clase, Inscripcion

admin.site.register(Socio)
admin.site.register(Profesor)
admin.site.register(Clase)
admin.site.register(Inscripcion)
