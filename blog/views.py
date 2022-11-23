from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView #10

posts=[
	{
		'autor':'Fede',
		'titulo': 'post 1',
		'content': 'primer post',
		'fecha': '22 de noviembre, 2022',
	},
    {
		'autor':'Luis',
		'titulo': 'post 2',
		'content': 'segundo post',
		'fecha': '23 de noviembre, 2022'
	}
]


def home(request):
    context={ 'posts':Post.objects.all()}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):#10
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	#ordering = ['-date_posted']

class PostDetailView(DetailView):#10
	model = Post

def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
