from django.shortcuts import render
from django.http import HttpRequest
from .models import ProductCategory, Product


# Create your views here.
def index(request: HttpRequest):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request: HttpRequest):
    return render(request, 'mainapp/products.html')

def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')

