from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'fecha_publicacion', 'fecha_creacion')
    list_filter = ('genero', 'fecha_publicacion', 'fecha_creacion')
    search_fields = ('titulo', 'autor')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    ordering = ('-fecha_creacion',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'autor', 'genero')
        }),
        ('Fechas', {
            'fields': ('fecha_publicacion', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    def get_genero_display(self, obj):
        return obj.get_genero_display()
    get_genero_display.short_description = 'Género'
