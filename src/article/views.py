from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Comment
# Create your views here.

class ArticlesListView(TemplateView):
    template_name = 'article/home.html'
    model = Article
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'headline_article': Article.get_headline_article(self),
            'featured_latest_two': Article.objects.filter(featured=True).order_by('-publish_date')[:2]
        }) 
        return context
    