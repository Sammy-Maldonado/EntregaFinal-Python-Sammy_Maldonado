from django.urls import path
from AppCoder import views

app_name = 'AppCoder'

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', views.CursoListView.as_view(), name="cursos"),
    path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso_detail'),
    path('cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='curso_delete'),
    path('profesores/', views.profesores, name="profesores"),
    path('entregables/', views.entregables, name="entregables"),
    path('estudiante/crear/', views.EstudianteCreateView.as_view(), name='estudiante_crear'),
    #path('listaEstudiantes/', views.lista_estudiantes, name="estudiantes"),
    path('estudiantes/', views.EstudianteListView.as_view(), name='lista_estudiantes'),  #vista basada en clases
    #path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('estudiante/<int:pk>/', views.EstudianteDetailView.as_view(), name='estudiante_detail'),
    #path('estudiante/actualizar/<int:pk>/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('estudiante/editar/<int:pk>/', views.EstudianteUpdateView.as_view(), name='estudiante_actualizar'),
    path('estudiante/eliminar/<int:pk>/', views.EstudianteDeleteView.as_view(), name='estudiante_delete'),
    path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    path('buscarCurso/', views.buscarCurso, name='buscarCurso'),
]