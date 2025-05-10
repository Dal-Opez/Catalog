from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductsByCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('catalog/create', ProductCreateView.as_view(), name='products_create'),
    path('catalog/update/<int:pk>/', ProductUpdateView.as_view(), name='products_update'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='products_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category')
]