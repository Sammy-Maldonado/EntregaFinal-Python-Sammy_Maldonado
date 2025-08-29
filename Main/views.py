from django.shortcuts import render
from AppBlog.models import Post


def index(request):
    # Mostrar últimos 3 posts como destacados
    posts = Post.objects.all().order_by('-fecha_publicacion')[:3]
    return render(request, 'Main/index.html', {'posts': posts})