from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from main.models import Product, Category


def category(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'categories': categories})


def product(request, id: int):
    if id > len(Category.objects.all()):
        return HttpResponseNotFound('Wrong number')
    products = Product.objects.filter(category_id=id)
    return render(request, 'products.html', context={'products': products})


def cart(request):
    return render(request, 'cart.html')
