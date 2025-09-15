from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Main'

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil', views.perfil, name='perfil'),
    path('about', views.about, name='about'),
    path('editar-perfil', views.editar_perfil, name='editar_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='Main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Main:login'), name='logout'),
     path('crear-usuario/', views.CreateUserView.as_view(), name='crear_usuario'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)