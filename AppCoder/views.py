from django.shortcuts import render
from AppCoder.models import Curso 
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.models import Profesor
from AppCoder.forms import Profesor_formulario 
# Create your views here.



def inicio(request):
    return render( request , "padre.html")



def alta_cursos(request,nombre):
    cursos = Curso(nombre=nombre , camada=234512)
    cursos.save()
    texto = f"se guardo en la BD el curso: {cursos.nombre} {cursos.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)




def alumnos(request):
    return render(request , "alumnos.html")




def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")



def buscar_curso(request):
    return render(request, "buscar_curso.html")





def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre_icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse ("Ingrese el nombre del curso")





def alta_profesores(request,nombre):
    profesores = Profesor(nombre=nombre , profesor=123)
    profesores.save()
    texto = f"se guardo en la BD el curso: {profesores.nombre} {profesores.profesor}"
    return HttpResponse(texto)


def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)




def buscar_profesor(request):
    return render(request, "buscar_profesor.html")





def profesor_formulario(request):
    mi_formulario = Profesor_formulario()
    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            profesores = Profesor( nombre=datos["nombre"] , profesor=datos["profesor"])
            profesores.save()
            return render(request , "formulario.html")


    return render(request , "profes_formulario.html", {"form": mi_formulario})   

def buscar_profe(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesor = Profesor.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"profesores":profesor})
    else:
        return HttpResponse ("Ingrese el nombre del profesor")
    
def alumno_formulario(request):
    mi_formulario = alumno_formulario()
    if request.method == "POST":

        mi_formulario =alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            alumno = alumno( nombre=datos["nombre"] , alumno=datos["alumno"])
            alumno.save()
            return render(request , "formulario.html")


    return render(request , "alumno_formulario.html", {"form": mi_formulario})

def buscar_alumno(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumno = alumno.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"alumno":alumno})
    else:
        return HttpResponse ("Ingrese el nombre del alumno")
    

def alumnos(request):
    return render(request , "alumnos.html")

