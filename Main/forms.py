from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Avatar

class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=False, label='Nombre')
    last_name = forms.CharField(required=False, label='Apellido')
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class CreateUserForm(forms.ModelForm):  # Nuevo formulario para registrar usuarios
    username = forms.CharField(
        required=True,
        label='Nombre de usuario',
        help_text='',  # Elimina el mensaje predeterminado
    )
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=False, label='Nombre')
    last_name = forms.CharField(required=False, label='Apellido')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        # hashear la contraseña correctamente
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user