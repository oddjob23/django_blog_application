from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Comment
# Create your views here.

class ArticlesListView(ListView):
    template_name = 'article/article_list.html'
    model = Article
    context_object_name = 'articles'
