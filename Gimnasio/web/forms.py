from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Inscripcion, Clase, Socio
from django.contrib.auth import get_user_model

User = get_user_model()



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


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['user', 'dni', 'plan']

    PLANES = (
        ('BASICO', 'Básico'),
        ('PREMIUM', 'Premium'),
        ('ESTANDAR', 'Estandar'),
    )
    plan = forms.ChoiceField(choices=PLANES)

    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)
        self.fields['dni'].widget.attrs.update({"class": "form-control"})
        self.fields['plan'].widget.attrs.update({"class": "form-control"})

        if self.instance and self.instance.pk:
            self.fields['user'].widget = forms.HiddenInput()
        else:
            self.fields['user'].queryset = User.objects.all()
            self.fields['user'].widget.attrs.update({"class": "form-control"})

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if not isinstance(dni, int):
            try:
                dni = int(dni)
            except ValueError:
                raise ValidationError("El DNI debe ser un número de 7 a 8 dígitos.")

        if not (1000000 <= dni < 100000000):
            raise ValidationError("El DNI debe ser un número de 7 a 8 dígitos.")
        return dni
        dni = self.cleaned_data.get("dni")
        if not (1000000 <= dni < 100000000):
            raise ValidationError("El DNI debe ser un número de 7 a 8 dígitos.")
        return dni

    def clean_user(self):
        if self.instance and self.instance.pk:
            return self.instance.user
        return self.cleaned_data['user']

class ProfesorForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Usuario", required=True)
    dni = forms.CharField(label="Dni", max_length=8, required=True)
    telefono = forms.CharField(label="Telefono", max_length=15, required=True)

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")

        if not (1000000 <= int(dni) < 100000000):
            raise forms.ValidationError("El DNI debe ser un número de 7 a 8 dígitos.")
        
        return dni


class InscripcionForm(forms.ModelForm):
    clase = forms.ModelChoiceField(queryset=Clase.objects.all(), label="Clase")
    socio = forms.ModelChoiceField(queryset=Socio.objects.all(), label="Socio")

    class Meta:
        model = Inscripcion
        fields = ["clase", "socio"]
