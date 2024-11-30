from django.urls import path

from AppCoder import views
from AppCoder import views_clases
from AppCoder.views_clases import CursoListView
from django.contrib.auth.views import LogoutView  # pylint: disable=import-error


urlpatterns = [
    # Le damos un nuevo argumento, indicando el nombre de la vista. para que al tocar cada boton, django sepa a donde ir.
    path('inicio/', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    path('cursoFormulario2/', views.cursoFormulario2, name='cursoFormulario2'),
    path('busquedaCamada/', views.busquedaCamada, name='busquedaCamada'),
    path('buscar/', views.buscar, name='buscar'),
    path('leerProfesores/', views.leerProfesores, name='leerProfesores'),
    path('profesorFormulario', views.Profesores, name='profesorFormulario'),
    path('eliminar_profesor/<int:id>/',
         views.eliminar_profesor, name='eliminarProfesor'),
    path('editarProfesor/<int:id>/', views.editar_profesor, name='editarProfesor'),
    path('login/', views_clases.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(), name="Logout"),
]

urls_vistas_clases = [
    path('clases/lista/', CursoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/',
         views_clases.CursoDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.CursoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>',
         views_clases.CursoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>',
         views_clases.CursoDeleteView.as_view(), name='Delete')
]

urlpatterns += urls_vistas_clases
