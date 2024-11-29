from django import forms
from django.contrib.auth.forms import UserCreationForm  # Importa UserCreationForm
# Importa el modelo User si es necesario
from django.contrib.auth.models import User
from .models import Profesor


class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=20)


class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesor  # Indica que este formulario está basado en el modelo Profesor
        # Especifica los campos del modelo a incluir en el formulario
        fields = ['nombre', 'apellido', 'email', 'profesion']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir contraseña', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ["username", "email", "password", "password2"]
    #     help_text = {k: "" for k in fields}
