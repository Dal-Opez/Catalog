from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import get_products_by_category, get_products_from_cache

# Create your views here.


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.is_superuser:
            class DynamicProductForm(ProductForm):
                class Meta(ProductForm.Meta):
                    exclude = ['created_at', 'updated_at', 'is_published'] if not user.is_superuser else []
            return DynamicProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

        raise PermissionDenied


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        self.object = self.get_object()
        if not (user.has_perm('catalog.can_delete_product') or user.is_superuser or user==self.object.owner):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
        return HttpResponse(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
        return HttpResponse(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
    return render(request, 'catalog/contacts.html')


class ProductsByCategoryView(ListView):
    model = Category
    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return get_products_by_category(category_id=category_id)