from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Estudiante, Curso, Calificaciones

admin.site.register(Estudiante, list_display=('nombre', 'apellido', 'correo'))
admin.site.register(Curso)
admin.site.register(Calificaciones)
