from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Libro(models.Model):
    GENERO_CHOICES = [
        ('ficcion', 'Ficción'),
        ('no_ficcion', 'No Ficción'),
        ('misterio', 'Misterio'),
        ('romance', 'Romance'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('fantasia', 'Fantasía'),
        ('biografia', 'Biografía'),
        ('historia', 'Historia'),
        ('filosofia', 'Filosofía'),
        ('poesia', 'Poesía'),
        ('teatro', 'Teatro'),
        ('infantil', 'Infantil'),
        ('juvenil', 'Juvenil'),
        ('tecnologia', 'Tecnología'),
        ('autoayuda', 'Autoayuda'),
        ('otros', 'Otros'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES, verbose_name="Género")
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
    def get_genero_display(self):
        return dict(self.GENERO_CHOICES)[self.genero]
