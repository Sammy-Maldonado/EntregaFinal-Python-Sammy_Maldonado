from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from AppBlog.models import Post

from .forms import EditUserForm, AvatarForm, CreateUserForm
from .models import Avatar

@login_required
def index(request):
    # Mostrar últimos 3 posts como destacados
    posts = Post.objects.all().order_by('-fecha_publicacion')[:3]
    return render(request, 'Main/index.html', {'posts': posts})

def perfil(request):
    return render(request, 'Main/perfil.html')

def about(request):
    return render(request, 'Main/about.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Distinguimos qué formulario se envía por el name del botón
        if 'save_profile' in request.POST:
            form = EditUserForm(request.POST, instance=request.user)
            
            try:
                avatar = request.user.avatar
            except Avatar.DoesNotExist:
                avatar = None

            if avatar:
                avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
            else:
                avatar_form = AvatarForm(request.POST, request.FILES)

            password_form = PasswordChangeForm(user=request.user)  # vacío para re-render

            if form.is_valid() and avatar_form.is_valid():
                form.save()
                avatar_instance = avatar_form.save(commit=False)
                avatar_instance.user = request.user
                avatar_instance.save()
                messages.success(request, "Perfil actualizado correctamente.")
                return redirect('Main:perfil')
        elif 'change_password' in request.POST:
            form = EditUserForm(instance=request.user)
            if hasattr(request.user, 'avatar'):
                avatar_form = AvatarForm(instance=request.user.avatar)
            else:
                avatar_form = AvatarForm()

            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # mantiene la sesión activa
                messages.success(request, "Contraseña actualizada correctamente.")
                return redirect('Main:perfil')
            else:
                messages.error(request, "Corrige los errores en el formulario de contraseña.")
        else:
            # fallback: reconstruir formularios
            form = EditUserForm(request.POST, instance=request.user)
            password_form = PasswordChangeForm(user=request.user)
            avatar_form = AvatarForm(request.POST, request.FILES)
    else:
        form = EditUserForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()

    return render(
        request,
        "Main/editar_perfil.html",
        {'form': form, 'avatar_form': avatar_form, 'password_form': password_form}
    )
    
class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'Main/crear_usuario.html'
    success_url = reverse_lazy('Main:login')  # Redirige al login después de crear el usuario