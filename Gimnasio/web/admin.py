from django.contrib import admin
from .models import Clase, Socio, Inscripcion, Profesor

admin.site.register(Clase)
admin.site.register(Socio)
admin.site.register(Inscripcion)
admin.site.register(Profesor)
