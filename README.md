# Tercera Entrega - Sammy Maldonado

Este proyecto es una aplicación web desarrollada con Django que incluye dos aplicaciones principales: **AppCoder** y **AppBlog**.

## Estructura del Proyecto

- **AppCoder**: Gestión de cursos y estudiantes.
- **AppBlog**: Gestión de publicaciones de blog.

---

## 1. Instalación

1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
4. Crea un superusuario para acceder al admin:
   ```bash
   python manage.py createsuperuser
   ```
5. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

---

## 2. Funcionalidades y Orden de Prueba

### AppCoder

- **Gestión de Cursos**
  - Formulario: `AppCoder/forms.py` (`CursoFormulario`)
  - Prueba: Accede a la vista de cursos, agrega y busca cursos por camada.

- **Búsqueda de Cursos**
  - Formulario: `AppCoder/forms.py` (`BusquedaCursoFormulario`)
  - Prueba: Utiliza el formulario de búsqueda para filtrar cursos por camada.

- **Gestión de Estudiantes**
  - Formulario: `AppCoder/forms.py` (`EstudianteForm`)
  - Prueba: Agrega estudiantes usando el formulario basado en el modelo `Estudiante`.

### AppBlog

- **Gestión de Publicaciones**
  - Modelo: `AppBlog/models.py` (`Post`)
  - Prueba: Desde el admin de Django, crea, edita y elimina publicaciones.
  - Campos importantes: título, contenido, fecha de publicación, autor, estado (borrador/publicado).

---

## 3. Orden Sugerido de Pruebas

1. **Admin de Django**
   - Ingresa como superusuario.
   - Crea cursos y estudiantes desde el admin.
   - Crea publicaciones de blog.

2. **Formularios de AppCoder**
   - Prueba el formulario de creación de cursos.
   - Prueba la búsqueda de cursos por camada.
   - Prueba el formulario de creación de estudiantes.

3. **AppBlog**
   - Crea y publica posts desde el admin.
   - Verifica los estados de publicación (borrador/publicado).

---

## 4. Ubicación de Archivos Clave

- **Modelos**:  
  - `AppCoder/models.py`  
  - `AppBlog/models.py`

- **Formularios**:  
  - `AppCoder/forms.py`

- **Vistas y URLs**:  
  - `AppCoder/views.py`, `AppCoder/urls.py`  
  - `AppBlog/views.py`, `AppBlog/urls.py`

---

## 5. Notas

- Asegúrate de tener configurada la base de datos en `settings.py`.
- Puedes personalizar las vistas y plantillas según tus necesidades.

---

¡Listo para probar y desarrollar!