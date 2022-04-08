from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'

class PostListView(generic.ListView): 
    model = Post 