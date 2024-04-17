from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("buscar_alumno", views.buscar_alumno),
    path("buscar", views.buscar_alumno, name="buscar_alumno"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar_profesor", views.buscar_profesor),
    path("alta_profe", views.profesor_formulario, name="alta_profe"),
    path("buscar_profesor", views.buscar_profesor),
    path("buscar", views.buscar_profe, name="buscar_profe"),
    path("buscar", views.buscar)
]
