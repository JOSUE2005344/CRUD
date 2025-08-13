from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'libros', views.LibroViewSet)

urlpatterns = [
    # URLs para formularios Django (interfaz principal)
    path('', views.index, name='index'),
    path('libro/nuevo/', views.crear_libro, name='crear_libro'),
    path('libro/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libro/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    
    # URLs para API REST (mantener para uso futuro)
    path('api/', include(router.urls)),
]
