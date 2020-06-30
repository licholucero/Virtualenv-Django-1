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

class LibroAdmin(admin.ModelAdmin):
    #filter_vertical = ('titulo' ,)
    list_display = ['titulo', 'editorial',]
     
class LibroInLine(admin.ModelAdmin):
    model = libro

class AutorAdmin(admin.ModelAdmin):
    #list_display = []
    inlines = [LibroInLine,]
    search_fields = ['nombre', 'libro_titulo', 'libro_editorial']

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario,UsuariosAdmin)