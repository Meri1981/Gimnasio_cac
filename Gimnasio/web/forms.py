from django import forms

class RegistrarseForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput(), required=True)