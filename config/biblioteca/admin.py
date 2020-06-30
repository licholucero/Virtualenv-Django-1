from django.contrib import admin

from. models import *
# Register your models here.

class UsuariosAdmin(admin.MoldelAdmin):
    #exclude = ['codigo', 'telefono']
    fieldsets = (
        ('Datos', {
            'fields': ('nombre',)
        }),
        ('Contacto' , {
            'fields': ('telefono', 'direccion')
        })
    )
    list_display = ['nombre', 'telefono', 'direccion']

class EjemplarAdmin(admin.ModelAdmin):
    list_filter = ['libro',]



admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Ejemplar)
admin.site.register(Usuario)