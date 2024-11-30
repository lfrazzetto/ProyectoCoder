from django.shortcuts import render  # Para renderizar plantillas HTML
from .models import Curso  # Importa el modelo "Curso" desde tu aplicación
from django.views.generic import ListView  # Para mostrar listas de objetos
# Para mostrar detalles de un objeto
from django.views.generic.detail import DetailView
# Para crear, actualizar y eliminar objetos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  # Para generar URLs de forma segura

# Formularios de autenticación de usuarios
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Funciones para gestionar inicios de sesión y autenticación
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin


def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":  # Si el formulario fue enviado (método POST)
        # Crea un formulario y lo llena con los datos enviados
        form = AuthenticationForm(request, data=request.POST)
        print(form)  # Imprime el formulario en la consola (para depuración)

        if form.is_valid():  # Si el formulario es válido
            # Obtiene el nombre de usuario
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")  # Obtiene la contraseña

            # Intenta autenticar al usuario
            nombre_usuario = authenticate(username=usuario, password=clave)

            if nombre_usuario is not None:  # Si la autenticación es exitosa
                login(request, nombre_usuario)  # Inicia la sesión del usuario
                # Renderiza la plantilla con un mensaje de bienvenida
                return render(request, "AppCoder/cursos.html", {"mensaje": f"Has iniciado sesión. Bienvenido {usuario}"})
            else:  # Si la autenticación falla
                form = AuthenticationForm()  # Crea un nuevo formulario vacío
                # Renderiza el formulario de login con un mensaje de error
                return render(request, "AppCoder/login.html", {"mensaje": "Error, datos incorrectos", "form": form})
        else:  # Si el formulario no es válido
            # Renderiza la plantilla con un mensaje de error
            return render(request, "AppCoder/index.html", {"mensaje": "Error, formulario inválido"})

    # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    form = AuthenticationForm()
    # Renderiza el formulario de login
    return render(request, "AppCoder/login.html", {"form": form})


class CursoListView(LoginRequiredMixin, ListView):
    """
    Vista para mostrar una lista de todos los cursositos.
    """
    model = Curso  # Modelo con el que trabaja esta vista
    # Plantilla para renderizar la lista
    template_name = "AppCoder/Vistas_Clases/curso_list.html"


class CursoDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_detalle.html"


class CursoCreateView(CreateView):
    """
    Vista para crear nuevos cursos a través de un formulario.
    """
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_form.html"
    # URL de redirección después de crear un curso
    success_url = reverse_lazy("List")
    # Campos del modelo a mostrar en el formulario
    fields = ["nombre", "camada"]


class CursoUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_edit.html"
    success_url = reverse_lazy("List")
    # success_url = "/clases/lista/"  # Otra forma de especificar la URL de redirección
    fields = ["nombre", "camada"]


class CursoDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Curso
    # URL de redirección después de eliminar un curso
    success_url = reverse_lazy("List")
    # Plantilla para confirmar la eliminación
    template_name = "AppCoder/Vistas_Clases/curso_confirm_delete.html"
