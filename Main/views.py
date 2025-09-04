from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppBlog.models import Post

from .forms import EditUserForm, AvatarForm
from .models import Avatar

def index(request):
    # Mostrar últimos 3 posts como destacados
    posts = Post.objects.all().order_by('-fecha_publicacion')[:3]
    return render(request, 'Main/index.html', {'posts': posts})

def perfil(request):
    return render(request, 'Main/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        
        # Verificar si el usuario tiene un avatar
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
            
        # Crear el formulario de avatar según si el usuario tiene uno o no
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user     # Asignar el usuario actual al avatar
            avatar_instance.save()
            return redirect('Main:perfil')
    else:
        form = EditUserForm(instance=request.user)
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(
        request, "Main/editar_perfil.html", {'form': form, 'avatar_form': avatar_form}
    )
    
    
    return render(request, 'Main/editar_perfil.html', {'form': form})