from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Libro
from .forms import LibroForm, BusquedaForm
from .serializers import LibroSerializer, LibroCreateSerializer

# Vista principal con formularios Django
def index(request):
    """Vista principal para la interfaz web con formularios Django"""
    # Obtener parámetros de búsqueda
    search = request.GET.get('search', '')
    genero = request.GET.get('genero', '')
    # Siempre ordenar por ID ascendente (1, 2, 3...)
    
    # Filtrar libros
    libros = Libro.objects.all()
    
    if search:
        libros = libros.filter(
            Q(titulo__icontains=search) |
            Q(autor__icontains=search) |
            Q(genero__icontains=search)
        )
    
    if genero:
        libros = libros.filter(genero=genero)
    
    # Ordenar siempre por ID ascendente
    libros = libros.order_by('id')
    
    # Calcular estadísticas
    total_libros = Libro.objects.count()
    generos_count = {}
    for genero_choice in Libro.GENERO_CHOICES:
        count = Libro.objects.filter(genero=genero_choice[0]).count()
        if count > 0:
            generos_count[genero_choice[1]] = count
    
    # Calcular libros de este año
    from datetime import date
    current_year = date.today().year
    libros_este_ano = libros.filter(fecha_publicacion__year=current_year).count()
    
    # Formulario de búsqueda
    busqueda_form = BusquedaForm(request.GET)
    
    context = {
        'libros': libros,
        'busqueda_form': busqueda_form,
        'total_libros': total_libros,
        'total_generos': len(generos_count),
        'libros_este_ano': libros_este_ano,
        'generos_count': generos_count,
    }
    
    return render(request, 'index.html', context)

def crear_libro(request):
    """Crear un nuevo libro"""
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            messages.success(request, f'Libro "{libro.titulo}" creado exitosamente.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = LibroForm()
    
    return render(request, 'libro_form.html', {
        'form': form,
        'titulo': 'Nuevo Libro',
        'accion': 'Crear'
    })

def editar_libro(request, libro_id):
    """Editar un libro existente"""
    libro = get_object_or_404(Libro, id=libro_id)
    
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            messages.success(request, f'Libro "{libro.titulo}" actualizado exitosamente.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = LibroForm(instance=libro)
    
    return render(request, 'libro_form.html', {
        'form': form,
        'libro': libro,
        'titulo': 'Editar Libro',
        'accion': 'Actualizar'
    })

def eliminar_libro(request, libro_id):
    """Eliminar un libro"""
    libro = get_object_or_404(Libro, id=libro_id)
    
    if request.method == 'POST':
        titulo = libro.titulo
        libro.delete()
        messages.success(request, f'Libro "{titulo}" eliminado exitosamente.')
        return redirect('index')
    
    return render(request, 'libro_confirm_delete.html', {
        'libro': libro
    })

# Mantener las vistas de API REST para uso futuro
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LibroCreateSerializer
        return LibroSerializer
    
    def list(self, request, *args, **kwargs):
        """Listar todos los libros con opciones de filtrado"""
        queryset = self.get_queryset()
        
        # Filtro por género
        genero = request.query_params.get('genero', None)
        if genero:
            queryset = queryset.filter(genero=genero)
        
        # Búsqueda por título, autor o género
        search = request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) |
                Q(autor__icontains=search) |
                Q(genero__icontains=search)
            )
        
        # Ordenamiento
        ordering = request.query_params.get('ordering', '-fecha_creacion')
        if ordering:
            queryset = queryset.order_by(ordering)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        """Crear un nuevo libro"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            libro = serializer.save()
            response_serializer = LibroSerializer(libro)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        """Actualizar un libro existente"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            libro = serializer.save()
            response_serializer = LibroSerializer(libro)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        """Eliminar un libro"""
        instance = self.get_object()
        instance.delete()
        return Response(
            {'mensaje': 'Libro eliminado exitosamente'}, 
            status=status.HTTP_204_NO_CONTENT
        )
    
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """Obtener estadísticas de los libros"""
        total_libros = Libro.objects.count()
        generos_count = {}
        
        for genero_choice in Libro.GENERO_CHOICES:
            count = Libro.objects.filter(genero=genero_choice[0]).count()
            if count > 0:
                generos_count[genero_choice[1]] = count
        
        return Response({
            'total_libros': total_libros,
            'generos_count': generos_count
        })
    
    @action(detail=False, methods=['get'])
    def generos(self, request):
        """Obtener lista de géneros disponibles"""
        return Response({
            'generos': [{'codigo': choice[0], 'nombre': choice[1]} 
                       for choice in Libro.GENERO_CHOICES]
        })
