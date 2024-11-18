from django.shortcuts import render
from django.http import HttpResponse


def inicio(req):
    return render(req, 'appcoder/index.html')


def cursos(req):
    return render(req, 'appcoder/cursos.html')


def profesores(req):
    return HttpResponse('vista profesores')


def estudiantes(req):
    return HttpResponse('vista estudiantes')


def entregables(req):
    return HttpResponse('vista entregables')
