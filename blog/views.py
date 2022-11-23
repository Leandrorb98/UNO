from django.shortcuts import render
from django.http import HttpResponse


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
    context={ 'posts':posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
