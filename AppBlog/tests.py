from django.test import TestCase
from django.urls import reverse_lazy
from AppBlog.views import PostCreateView
from .models import Post, User

class PostTests(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(titulo="Python", auto=self.user)

#Esta prueba unitaria que verifica que lo que hace el codigo escrito en el primer parametro, hace lo que se define en el segundo parametro. En este caso, verifica que la URL de éxito de la vista PostCreateView es igual a la URL resuelta para "AppBlog:post_list".
class PostCreateViewTests(TestCase):
    def test_success_url(self):
        url = reverse_lazy("AppBlog:post_list")
        self.assertEqual(PostCreateView.success_url, url)
