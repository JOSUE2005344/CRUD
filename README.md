# grupo 5 MB5 - CRUD/Gestion de libros 

## 🎯 Product Backlog
Desarrollar un sistema de gestion de libros que permita: 
- Agregar libros
- Poder ver los libros registrados
- Actualizar la informacion de libros previamente registrados
- Eliminar libros registrados

## 🎯 Sprint Goal
Entregar un CRUD funcional de gestión de libros con operaciones de agregar, listar, actualizar y eliminar, cumpliendo con criterios de aceptación y documentado con Scrum.

## 👥 Roles Scrum
| Rol            | Integrante           | Función principal                                                                                                 |
|----------------|---------------------|------------------------------------------------------------------------------------------------------------------|
| Scrum Master   | INTEGRANTE 1    | Facilita el proceso Scrum, elimina impedimentos y asegura que el equipo siga los principios ágiles.              |
| Product Owner  | Gianluca Revilla     | Define Historias de usuario, prioriza funcionalidades y establece las metas del proyecto.                        |
| Developer 1    | INTEGRANTE 3       | Desarrolla la estructura de las plantillas HTML para la interfaz de usuario.                                     |
| Developer 2    | INTEGRANTE 4      | Diseña y desarrolla los estilos CSS personalizados en la carpeta static/css.                                     |
| Developer 3    | INTEGRANTE 5  | Se encarga de la creación y configuración del proyecto Django, así como de la lógica principal del backend.      |

## 🎯 Características Principales

### ✅ **Funcionalidades CRUD**
- **Crear** nuevos libros con validación de datos
- **Leer** lista de libros con filtros y búsqueda
- **Actualizar** información de libros existentes
- **Eliminar** libros con confirmación

### ✅ **Interfaz de Usuario**
- **Diseño responsivo** con Bootstrap 5
- **Formularios Django puros** (sin JavaScript)
- **Búsqueda en tiempo real** por título, autor o género
- **Filtros por género** con dropdown
- **Ordenamiento fijo** por ID (1, 2, 3...)
- **Estadísticas automáticas** de la biblioteca

### ✅ **Características Técnicas**
- **Backend**: Django 4.2.7
- **Base de datos**: SQLite
- **API REST**: Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap 5
- **Validación**: Formularios Django con validación personalizada

## 📋 Campos Obligatorios

Cada libro debe contener:
- **Título** (mínimo 2 caracteres)
- **Autor** (mínimo 2 caracteres)
- **Género** (selección de lista predefinida)
- **Fecha de Publicación** (no puede ser futura)

## 🏗️ Estructura del Proyecto

```
Proyecto CRUD/
├── gestion_libros/          # Proyecto Django principal
│   ├── __init__.py
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # URLs principales
│   └── wsgi.py
├── libros/                  # Aplicación de libros
│   ├── __init__.py
│   ├── admin.py             # Configuración del admin
│   ├── apps.py
│   ├── forms.py             # Formularios Django
│   ├── models.py            # Modelo Libro
│   ├── serializers.py       # Serializers para API
│   ├── urls.py              # URLs de la app
│   └── views.py             # Vistas y lógica
├── static/                  # Archivos estáticos
│   └── css/
│       └── styles.css       # Estilos personalizados
├── templates/               # Plantillas HTML
│   ├── index.html           # Página principal
│   ├── libro_form.html      # Formulario crear/editar
│   └── libro_confirm_delete.html  # Confirmación eliminar
├── manage.py               # Script de gestión Django
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## 🚀 Instalación y Configuración

### 1. **Clonar o Descargar el Proyecto**
```bash
# Navegar al directorio del proyecto
cd "Proyecto CRUD"
```

### 2. **Crear Entorno Virtual**
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate


### 3. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### 4. **Configurar Base de Datos**
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 5. **Crear Superusuario (Opcional)**
```bash
python manage.py createsuperuser
```

### 6. **Ejecutar el Servidor**
```bash
python manage.py runserver
```

## 🌐 Acceso al Sistema

Una vez ejecutado el servidor, puedes acceder a:

- **Interfaz Principal**: http://localhost:8000
- **Admin Django**: http://localhost:8000/admin
- **API REST**: http://localhost:8000/api/libros/

### Historia de Usuario 1: Agregar libro

Como usuario, quiero poder agregar un nuevo libro a la biblioteca, para tener un registro actualizado de los libros disponibles.

**criterios de aceptacion** 
- El formulario de creación de libro debe estar disponible desde la página principal.
- Todos los campos obligatorios del modelo Libro deben estar presentes en el formulario.
- El título debe visualizarse claramente y ser fácil de identificar.
- Debe existir un campo de búsqueda que permita filtrar libros por título.
- Si no hay libros registrados, la lista debe mostrar un mensaje indicándolo.

### Historia de Usuario 2: Libros registrados

Como usuario, quiero ver la lista de todos los libros registrados, para consultar fácilmente la información de cada libro.

**Criterios de aceptacion** 
- El nombre del autor debe visualizarse claramente junto al título del libro.
- La lista se actualiza automáticamente al agregar, editar o eliminar un libro.
- Cada libro muestra los campos principales definidos.

### Historia de Usuario 3: Actualizar informacion de libro

Como usuario, quiero editar la información de un libro existente, para corregir errores o actualizar datos.

**Criterios de aceptacion**
- Desde la lista de libros (index.html), existe un botón o enlace para editar cada libro.
- Al guardar los cambios, la información se actualiza en la base de datos y en la lista.
- Si los datos son inválidos, se muestra un mensaje de error.
  
### Historia de Usuario 4: Eliminar un libro

Como usuario, quiero poder eliminar un libro del sistema para mantener actualizada y limpio la base de datos.

**Criterios de aceptacion** 

- El sistema debe permitir seleccionar un libro y eliminarlo de la lista.
- Antes de eliminar, debe pedirse una confirmación para evitar eliminaciones accidentales.
- Desde la lista de libros (index.html), existe un botón o enlace para eliminar cada libro.
- El libro eliminado no debe aparecer en la lista después de la confirmación.
- Si se intenta eliminar un libro que ya no existe, debe mostrarse un mensaje de error.
- Al confirmar, el libro se elimina de la base de datos y desaparece de la lista.
- Si se cancela, no se realiza ningún cambio.
  
## 📖 Uso del Sistema

### **Página Principal**
- **Ver libros**: Lista ordenada por ID (1, 2, 3...)
- **Buscar**: Campo de búsqueda por título, autor o género
- **Filtrar**: Dropdown para filtrar por género específico
- **Estadísticas**: Información automática de la biblioteca

### **Crear Libro**
1. Hacer clic en "Nuevo Libro"
2. Llenar el formulario con los datos requeridos
3. Hacer clic en "Crear Libro"

### **Editar Libro**
1. Hacer clic en el botón "Editar" de cualquier libro
2. Modificar los campos necesarios
3. Hacer clic en "Actualizar Libro"

### **Eliminar Libro**
1. Hacer clic en el botón "Eliminar" del libro
2. Confirmar la eliminación en la página de confirmación
3. Hacer clic en "Eliminar Libro"

## 🔧 Configuración del Proyecto

### **Archivo settings.py**
```python
# Configuraciones principales
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Mexico_City'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'libros',
]
```

### **Modelo Libro**
```python
class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
```

## 🎨 Géneros Disponibles

El sistema incluye los siguientes géneros literarios:
- Ficción, No Ficción, Misterio, Romance
- Ciencia Ficción, Fantasía, Biografía, Historia
- Filosofía, Poesía, Teatro, Infantil, Juvenil
- Tecnología, Autoayuda, Otros

## 🔌 API REST

El proyecto incluye una API REST completa para integración con otros sistemas:

### **Endpoints Disponibles**
- `GET /api/libros/` - Listar todos los libros
- `POST /api/libros/` - Crear nuevo libro
- `GET /api/libros/{id}/` - Obtener libro específico
- `PUT /api/libros/{id}/` - Actualizar libro
- `DELETE /api/libros/{id}/` - Eliminar libro
- `GET /api/libros/estadisticas/` - Estadísticas de la biblioteca
- `GET /api/libros/generos/` - Lista de géneros disponibles

### **Ejemplo de Uso API**
```bash
# Obtener todos los libros
curl http://localhost:8000/api/libros/

# Crear un nuevo libro
curl -X POST http://localhost:8000/api/libros/ \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Don Quijote","autor":"Miguel de Cervantes","genero":"ficcion","fecha_publicacion":"1605-01-01"}'
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2.7
- **Base de Datos**: SQLite
- **API**: Django REST Framework 3.14.0
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **Iconos**: Font Awesome 6.4.0
- **Validación**: Formularios Django
- **Entorno**: Python 3.x

## 📝 Validaciones Implementadas

### **Validaciones de Formulario**
- Título y autor: mínimo 2 caracteres
- Fecha de publicación: no puede ser futura
- Campos obligatorios: título, autor, género, fecha
- Limpieza automática de espacios en blanco

### **Validaciones de Modelo**
- Longitudes máximas de campos
- Opciones predefinidas para género
- Fechas automáticas de creación y actualización

## 🎯 Características Especiales

### **Interfaz Sin JavaScript**
- **Formularios puros de Django**
- **Búsqueda y filtros con recarga de página**
- **Confirmaciones mediante formularios HTML**
- **Navegación tradicional con enlaces**

### **Diseño Responsivo**
- **Adaptable a móviles, tablets y desktop**
- **Bootstrap 5 para componentes modernos**
- **CSS personalizado para estilos únicos**
- **Iconos Font Awesome para mejor UX**

### **Estadísticas Automáticas**
- **Total de libros en la biblioteca**
- **Número de géneros únicos**
- **Libros publicados en el año actual**
- **Distribución por género**

## 🔒 Seguridad

- **Validación de formularios** en frontend y backend
- **Protección CSRF** habilitada
- **Sanitización de datos** automática
- **Validación de fechas** para evitar fechas futuras

## 📊 Base de Datos

### **Tabla Libro**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Identificador único |
| titulo | CharField | Título del libro |
| autor | CharField | Autor del libro |
| genero | CharField | Género literario |
| fecha_publicacion | DateField | Fecha de publicación |
| fecha_creacion | DateTimeField | Fecha de creación en BD |
| fecha_actualizacion | DateTimeField | Última actualización |

## 🚀 Script de Inicio Rápido

Para facilitar el inicio del proyecto, puedes usar:

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
python manage.py runserver

# Linux/Mac
source venv/bin/activate
python manage.py runserver
```


