from django.db import models

class Clase(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    profesor = models.CharField("Profesor", max_length=100)
    cupo = models.SmallIntegerField("Cupo")
    horarios = models.CharField("Horario", max_length=100)

