from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView)                      #10
from . import views

urlpatterns = [
    #path('', views.home, name='blog-home'), #10
    path('', PostListView.as_view(), name='blog-home'), #10
    path('post/<int:pk/', PostDetailView.as_view(), name='post-detail'), #10
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]


