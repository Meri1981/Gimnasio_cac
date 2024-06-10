from django.db import models

class Clase(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    profesor = models.CharField("Profesor", max_length=100)
    cupo = models.SmallIntegerField("Cupo")
    horarios = models.CharField("Horario", max_length=100)

class Socio(models.Model):
    nombre = models.CharField("Nombre", max_length=40)
    dni = models.CharField("Dni", max_length=8)
    email = models.EmailField("Email", max_length=30)
    plan = models.CharField("Plan", max_length=10)