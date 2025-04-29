from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

# Create your views here.
def home(request):
    last_products = Product.objects.order_by('created_at')[:5]
    for product in last_products:
        print(product)
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
        return HttpResponse(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
    return render(request, 'catalog/contacts.html')