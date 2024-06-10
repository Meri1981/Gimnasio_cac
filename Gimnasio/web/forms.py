from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class RegistrarseForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[EmailValidator(message="Ingrese un email válido")],
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(), required=True
    )
    confirmar_password = forms.CharField(
        label="Confirmar Password", widget=forms.PasswordInput(), required=True
    )

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]

    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")

        return self.cleaned_data["apellido"]

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("El password debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("El password ebe tener al menos un número.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("El password debe tener almenos una letra.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")
        if password and confirmar_password and password != confirmar_password:
            raise ValidationError("las contraseñas no coinciden")
        return self.cleaned_data


class ClaseForm(forms.Form):
    id = forms.IntegerField(label="id", required=False)
    id.widget.attrs.update({"readonly": True, "class": "form-control"})
    nombre = forms.CharField(label="Nombre", required=True)
    nombre.widget.attrs.update({"class": "form-control"})
    profesor = forms.CharField(label="Profesor", required=True)
    profesor.widget.attrs.update({"class": "form-control"})
    cupo = forms.IntegerField(
        label="Cupo",
        required=True,
        min_value=0,
        help_text="Cantidad de alumnos máximo por clase",
    )
    cupo.widget.attrs.update({"class": "form-control"})
    horario = forms.CharField(label="Horario", help_text="Horarios de la clase")
    horario.widget.attrs.update({"class": "form-control"})

    def clean_cupo(self):
        cupo = self.cleaned_data.get("cupo")
        if cupo > 15:
            raise ValidationError("Las clases deben tener 15 integrantes como máximo")

        return cupo


class SocioForm(forms.Form):
    id = forms.IntegerField(label="id")
    id.widget.attrs.update({"readonly": True, "class": "form-control"})
    nombre = forms.CharField(label="Nombre", required=True)
    nombre.widget.attrs.update({"class": "form-control"})
    dni = forms.IntegerField(label="Dni", required=True)
    dni.widget.attrs.update({"class": "form-control"})
    email = forms.CharField(label="Email", required=True)
    email.widget.attrs.update({"class": "form-control"})
    plan = forms.CharField(label="Plan")
    plan.widget.attrs.update({"class": "form-control"})

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]

    def clean_dni(self):
        if not self.cleaned_data["Dni"].isalpha():
            raise ValidationError("El DNI solo puede estar compuesto por números")
        
        if not (1000000 <= self.cleaned_data["dni"] < 100000000):
            raise ValidationError("El DNI debe ser un número de 7 a 8 dígitos.")

        return self.cleaned_data["Dni"]