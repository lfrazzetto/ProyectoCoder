from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def inicio(req):
    return render(req, 'appcoder/padre.html')


@login_required
def cursos(req):
    return render(req, 'appcoder/cursos.html')


@login_required
def profesores(req):
    return render(req, 'appcoder/profesores.html')


@login_required
def estudiantes(req):
    return render(req, 'appcoder/estudiantes.html')


@login_required
def entregables(req):
    return render(req, 'appcoder/entregables.html')


def cursoFormulario(req):
    if req.method == 'POST':

        curso = Curso(nombre=req.POST['curso'],
                      camada=req.POST['camada'])
        curso.save()
        return render(req, "appcoder/padre.html")

    return render(req, "appcoder/cursoFormulario.html")


def cursoFormulario2(request):
    if request.method == "POST":  # Si el formulario fue enviado
        # Creamos un objeto formulario con los datos enviados
        miFormulario = CursoFormulario(request.POST)
        # Imprimimos el formulario para depuración (opcional)
        print(miFormulario)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            # Obtenemos los datos limpios y validados
            informacion = miFormulario.cleaned_data
            # Creamos un objeto Curso
            curso = Curso(
                nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()  # Guardamos el curso en la base de datos
            # Redirigimos a la página de inicio
            return render(request, "AppCoder/index.html")
    else:
        # Creamos un formulario vacío para mostrarlo inicialmente
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario2.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):
    camada = request.GET.get("camada")  # Usamos .get() para evitar errores
    if camada:  # Verificamos si 'camada' tiene un valor
        cursos = Curso.objects.filter(camada=camada)
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        return render(request, "AppCoder/busquedaCamada.html", {"error": "Por favor ingrese una camada válida."})


def leerProfesores(request):
    profesores = Profesor.objects.all()  # trae todos los profesores
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)


def Profesores(request):
    if request.method == 'POST':
        # Aquí llega toda la información del HTML
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()

            # Vuelve al inicio o a donde quieran
            return redirect('leerProfesores')

    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el HTML

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})


def eliminar_profesor(request, id):  # La función debe aceptar 'id'
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    # Cambia 'inicio' por la vista a donde deseas redirigir
    return redirect('leerProfesores')


def editar_profesor(request, id):
    # Obtén el profesor por su ID
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        formulario = ProfesorFormulario(
            request.POST, instance=profesor)  # Instancia prellenada
        if formulario.is_valid():
            formulario.save()
            # Redirige a la lista de profesores
            return redirect('leerProfesores')
    else:
        # Formulario vacío prellenado con datos del profesor
        formulario = ProfesorFormulario(instance=profesor)

    return render(request, 'AppCoder/editarProfesor.html', {'formulario': formulario, 'profesor': profesor})


def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request, "AppCoder/index.html")

        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()
    return render(request, "AppCoder/registro.html",  {"form": form, "msg_register": msg_register})
