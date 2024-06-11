from django.db import models


class Clase(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    profesor = models.CharField("Profesor", max_length=100)
    cupo = models.SmallIntegerField("Cupo")
    horarios = models.CharField("Horario", max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.profesor} ({self.horarios})"


class Socio(models.Model):
    nombre = models.CharField("Nombre", max_length=40)
    dni = models.CharField("Dni", max_length=8)
    email = models.EmailField("Email", max_length=30)
    plan = models.CharField("Plan", max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"


class Profesor(models.Model):
    nombre = models.CharField("Nombre", max_length=40)
    dni = models.CharField("Dni", max_length=8)
    email = models.EmailField("Email", max_length=30)
    telefono = models.CharField("Plan", max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.dni}"


class Inscripcion(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
