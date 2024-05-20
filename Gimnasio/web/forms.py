from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class RegistrarseForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    email = forms.EmailField(label='Email',required=True, validators=[EmailValidator(message="Ingrese un email válido")])
    password = forms.CharField(label='Password',widget=forms.PasswordInput(), required=True)
    confirmar_password= forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(), required=True)



    def clean_nombre(self):
            if not self.cleaned_data["nombre"].isalpha():
                raise ValidationError("El nombre solo puede estar compuesto por letras")

            return self.cleaned_data["nombre"]
    

    
    def clean_apellido(self):
            if not self.cleaned_data["apellido"].isalpha():
                raise ValidationError("El apellido solo puede estar compuesto por letras")

            return self.cleaned_data["apellido"]
    

    def clean_password(self):
          password = self.cleaned_data.get('password')
          if len(password) < 8:
                raise ValidationError('El password debe tener al menos 8 caracteres.')
          if not any(char.isdigit() for char in password):
                raise ValidationError('El password ebe tener al menos un número.')
          if not any(char.isalpha() for char in password):
                raise ValidationError('El password debe tener almenos una letra.')
          return password
    


    def clean(self):
          cleaned_data = super().clean()
          password = cleaned_data.get('password')
          confirmar_password = cleaned_data.get('confirmar_password')
          if password and confirmar_password and password != confirmar_password:
                raise ValidationError("las contraseñas no coinciden")
          return self.cleaned_data

class ClaseForm(forms.Form):
    id = forms.IntegerField(label='id')
    id.widget.attrs.update({'readonly':True, 'class': "form-control"})
    nombre = forms.CharField(label='Nombre', required=True)
    nombre.widget.attrs.update({'class': 'form-control'})
    profesor = forms.CharField(label='Profesor', required=True)
    profesor.widget.attrs.update({'class': 'form-control'})
    cupo = forms.IntegerField(label='Cupo', required=True, min_value=0, help_text="Cantidad de alumnos máximo por clase")
    cupo.widget.attrs.update({'class': 'form-control'})
    horario = forms.CharField(label="Horario", help_text="Horarios de la clase")
    horario.widget.attrs.update({'class': 'form-control'})

