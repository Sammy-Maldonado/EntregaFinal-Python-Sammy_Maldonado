from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import CursoFormulario, BusquedaCursoFormulario, EstudianteForm
from .models import Estudiante, Profesor, Curso, Entregable


def inicio(request):
    return render(request, "AppCoder/inicio.html")

class CursoListView(ListView):
    model = Curso
    template_name = 'AppCoder/cursos.html'
    context_object_name = 'cursos'
    
class CursoDetailView(DetailView):
    model = Curso
    template_name = 'AppCoder/curso_detail.html'
    context_object_name = 'curso'

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'AppCoder/curso_confirm_delete.html'
    success_url = reverse_lazy('AppCoder:cursos')

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre']
            camada = form.cleaned_data['camada']
            
            # Guardar los datos en la base de datos
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
            
            return render(request, 'AppCoder/curso_exito.html')
    else:
        form = CursoFormulario()
    
    return render(request, 'AppCoder/curso_formulario.html', {'form': form})

def buscarCurso(request):
    if request.method == 'GET':
        form = BusquedaCursoFormulario(request.GET)

        if form.is_valid():
            camada = form.cleaned_data['camada']
            resultados = Curso.objects.filter(camada=camada)

            return render(
                request,
                'AppCoder/resultados_busqueda.html',
                {'resultados': resultados, 'form': form}
            )
    else:
        form = BusquedaCursoFormulario()

    return render(
        request,
        'AppCoder/buscar_curso.html',
        {'form': form}
    )

# CRUD
#Create
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'AppCoder/estudiante_crear.html', {'form': form})

class EstudianteCreateView(CreateView):       #Recrea a post_create (vista basada en clases)
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'AppCoder/estudiante_crear.html'
    success_url = reverse_lazy('AppCoder:lista_estudiantes')

#Read
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/lista_estudiantes.html', {'estudiantes': estudiantes})

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'AppCoder/lista_estudiantes.html'
    context_object_name = 'estudiantes'
    
def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'AppCoder/estudiante_detail.html', {'estudiante': estudiante})

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_detail.html'
    context_object_name = 'estudiante'

#Update
def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'AppCoder/actualizar_estudiante.html', {'form': form})

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    template_name = 'AppCoder/estudiante_actualizar.html'
    success_url = reverse_lazy('AppCoder:lista_estudiantes')

#Delete
def borrar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect('lista_estudiantes')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_confirm_delete.html'
    success_url = reverse_lazy('AppCoder:lista_estudiantes')