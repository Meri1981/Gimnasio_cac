from django import forms

class RegistrarseForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput(), required=True)

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
