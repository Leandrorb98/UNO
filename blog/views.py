from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView #10

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
	ordering = ['-fecha']
	#ordering = ['-date_posted'] si no funciona, probar con fecha en vez de date_posted

class PostDetailView(DetailView):#10
	model = Post

class PostCreateView(LoginRequired, MixinCreateView):#10
	model = Post
	fields = ['title','content']

	def form_valid (self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	 
class PostUpdateView(LoginRequiredMixin, UpdateView):#10
	model = Post
	fields = ['title','content']
	
	def form_valid (self, form):
	form.instance.author = self.request.user
	return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html')




# Create your views here.
