from django.contrib import admin
from django.urls import path

from estudiantes.views import agregar_estudiante, agregar_curso, agregar_calificacion, lista_estudiantes, lista_cursos, \
    lista_calificaciones, modificar_estudiante, eliminar_estudiante, modificar_calificacion, eliminar_calificacion, \
    modificar_curso, eliminar_curso
from webapp.views import bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='inicio'),
    path('agregar_estudiante/', agregar_estudiante, name='agregar_estudiante'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
    path('agregar_calificacion/', agregar_calificacion, name='agregar_calificacion'),
    path('lista_estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('lista_cursos/', lista_cursos, name='lista_cursos'),
    path('lista_calificaciones/', lista_calificaciones, name='lista_calificaciones'),
    path('modificar_estudiante/<int:estudiante_id>/', modificar_estudiante, name='modificar_estudiante'),
    path('eliminar_estudiante/<int:estudiante_id>/', eliminar_estudiante, name='eliminar_estudiante'),
    path('modificar_calificacion/<int:calificacion_id>/', modificar_calificacion, name='modificar_calificacion'),
    path('eliminar_calificacion/<int:calificacion_id>/', eliminar_calificacion, name='eliminar_calificacion'),
    path('modificar_curso/<int:curso_id>/', modificar_curso, name='modificar_curso'),
    path('eliminar_curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),

]
