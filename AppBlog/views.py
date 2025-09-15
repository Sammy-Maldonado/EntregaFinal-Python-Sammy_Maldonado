from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

#vista basada en funciones
def post_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        posts = Post.objects.filter(titulo__icontains=busqueda)
    else:
        posts = Post.objects.all()
    return render(request, 'AppBlog/post_list.html', {'posts': posts})

#vista basada en clases
class PostListView(ListView):
    model = Post
    template_name = 'AppBlog/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

def post_detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'AppBlog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('Main:index')
            else:
                form.add_error(None, "Debes estar logueado para crear una publicacion.")
    else:
        form = PostForm()
    return render(request, 'AppBlog/post_create.html', context={'form': form})

class PostCreateView(LoginRequiredMixin, CreateView):       #Recrea a post_create
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('AppBlog:post_list')
    login_url = reverse_lazy('Main:login')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.warning(self.request, "Debes estar logueado para crear una publicación.")
        return super().handle_no_permission()

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('AppBlog:post_list')
    login_url = reverse_lazy('Main:login')

    def handle_no_permission(self):
        messages.warning(self.request, "Debes estar logueado para editar una publicación.")
        return super().handle_no_permission()

class PostDetailView(DetailView):
    model = Post
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('AppBlog:post_list')