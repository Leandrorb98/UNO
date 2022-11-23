from django.urls import path
from .views import PostListView, PostDetailView#10
from . import views

urlpatterns = [
    #path('', views.home, name='blog-home'), #10
    path('', PostListView.as_view(), name='blog-home'), #10
    path('', PostDetailView.as_view(), name='blog-home'), #10
    path('about/', views.about, name='blog-about'),
]


