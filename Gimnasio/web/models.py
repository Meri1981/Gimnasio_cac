from django.db import models


class Profesor(models.Model):
    nombre = models.CharField("Nombre", max_length=40)
    dni = models.CharField("Dni", max_length=8)
    email = models.EmailField("Email", max_length=30)
    telefono = models.CharField("Telefono", max_length=15)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


class Clase(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    profesor = models.ForeignKey(
        Profesor, on_delete=models.CASCADE, null=True, blank=True
    )
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


class Inscripcion(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = ("clase", "socio")

    def __str__(self):
        return f'{self.socio} - {self.clase} - {self.fecha_inscripcion.strftime("%Y-%m-%d %H:%M:%S")}'
