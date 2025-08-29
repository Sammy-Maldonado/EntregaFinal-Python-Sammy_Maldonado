from django import forms
from .models import Estudiante

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    camada = forms.IntegerField()
    
class BusquedaCursoFormulario(forms.Form):
    camada = forms.IntegerField(label='Camada')
    
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']