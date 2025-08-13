from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'fecha_publicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título del libro'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del autor'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'genero': 'Género',
            'fecha_publicacion': 'Fecha de Publicación'
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo.strip()) < 2:
            raise forms.ValidationError("El título debe tener al menos 2 caracteres.")
        return titulo.strip()

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        if len(autor.strip()) < 2:
            raise forms.ValidationError("El autor debe tener al menos 2 caracteres.")
        return autor.strip()

    def clean_fecha_publicacion(self):
        fecha = self.cleaned_data['fecha_publicacion']
        from datetime import date
        if fecha > date.today():
            raise forms.ValidationError("La fecha de publicación no puede ser futura.")
        return fecha

class BusquedaForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título, autor o género...'
        }),
        label='Buscar'
    )
    
    genero = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los géneros')] + Libro.GENERO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Género'
    )
    

