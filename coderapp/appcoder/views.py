from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse



def curso(self, nombre, camada):
    
    curso=Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado!</p>
    """)

def lista_cursos(self):

    lista=Curso.objects.all()
    return render(self, "lista_cursos.html",{"lista_cursos":lista})