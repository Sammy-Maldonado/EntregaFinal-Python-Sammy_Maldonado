from django.urls import path
from . import views

app_name = 'AppBlog'

urlpatterns = [
    #path('post/list', views.post_list, name='post_list'),
    #path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/list', views.PostListView.as_view(), name='post_list'),  #vista basada en clases
    #path('post/create/', views.post_create, name='post_create'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
]