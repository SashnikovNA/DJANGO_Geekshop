from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    users = [
        {'name': 'John', 'age': 10},
        {'name': 'Artur', 'age': 20},
        {'name': 'David', 'age': 30},
    ]

    return render(request, 'mainapp/index.html', {'data': users})

def products(request: HttpRequest):
    return render(request, 'mainapp/products.html')

def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')

