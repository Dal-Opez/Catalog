from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render

from blogs.models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'is_published', 'views_count')
    success_url = reverse_lazy('blogs:blogs_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'is_published', 'views_count')
    success_url = reverse_lazy('blogs:blogs_list')

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blogs:blogs_list')