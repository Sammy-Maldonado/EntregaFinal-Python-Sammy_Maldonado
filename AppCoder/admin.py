from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Entregable


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')   # campos que se verán en la lista
    search_fields = ('nombre', 'apellido')           # campos por los que se podrá buscar


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'profesion')
    search_fields = ('nombre', 'apellido')


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'camada')
    search_fields = ('nombre',)


class EntregableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_entrega', 'entregado')
    search_fields = ('nombre',)


# Registro de modelos con su configuración
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Entregable, EntregableAdmin)