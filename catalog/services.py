from django.core.cache import cache

from .models import Product, Category
from config.settings import CACHE_ENABLED

def get_products_by_category(category_id):
    products = Product.objects.filter(category=Category.objects.get(pk=category_id))
    return products


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products