from django.urls import path
from blogs.apps import BlogsConfig
from blogs.models import Article
from blogs.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blogs_list'),
    path('blogs/<int:pk>/', ArticleDetailView.as_view(), name='blogs_detail'),
    path('blogs/create/', ArticleCreateView.as_view(), name='blogs_create'),
    path('blogs/<int:pk>/update', ArticleUpdateView.as_view(), name='blogs_update'),
    path('blogs/<int:pk>/delete', ArticleDeleteView.as_view(), name='blogs_delete'),
]