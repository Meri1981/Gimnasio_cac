from django.db import models
from Gimnasio import settings

class Clase(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    profesor = models.CharField("Profesor", max_length=100)
    cupo = models.SmallIntegerField("Cupo")
    horarios = models.CharField("Horario", max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.profesor} ({self.horarios})"


class Socio(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    PLAN = [
        ('BASICO', 'Básico'),
        ('PREMIUM', 'Premium'),
        ('ESTANDAR', 'Estandar'),
    ]

    dni = models.CharField("Dni", max_length=8)
    plan = models.CharField(
        max_length=10,
        choices=PLAN,
        default='BASICO',
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.first_name} - {self.dni}"


class Profesor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    dni = models.CharField("Dni", max_length=8)
    telefono = models.CharField("Plan", max_length=15)

    def __str__(self):
        return f"{self.user.first_name} {self.user.first_name} - {self.dni}"


class Inscripcion(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Clase: {self.clase.nombre} Socio: {self.socio} fecha: {self.fecha_inscripcion}"