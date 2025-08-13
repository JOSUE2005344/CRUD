from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    genero_display = serializers.CharField(source='get_genero_display', read_only=True)
    
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'genero', 'genero_display', 
                 'fecha_publicacion', 'fecha_creacion', 'fecha_actualizacion']
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']
    
    def validate_fecha_publicacion(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("La fecha de publicación no puede ser futura.")
        return value
    
    def validate_titulo(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El título debe tener al menos 2 caracteres.")
        return value.strip()
    
    def validate_autor(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El autor debe tener al menos 2 caracteres.")
        return value.strip()

class LibroCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'fecha_publicacion']
    
    def validate_fecha_publicacion(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("La fecha de publicación no puede ser futura.")
        return value
    
    def validate_titulo(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El título debe tener al menos 2 caracteres.")
        return value.strip()
    
    def validate_autor(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El autor debe tener al menos 2 caracteres.")
        return value.strip()
