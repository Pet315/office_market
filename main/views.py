from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from main.models import Product, Category, Cart


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


def edit_cart_product(id, way):
    if id > len(Product.objects.filter()):
        return HttpResponseNotFound('Wrong number')

    product = Cart.objects.filter(product_id=id)

    if len(product) == 0:
        quantity = 0
    else:
        quantity = product[0].quantity
    product.delete()

    cart = Cart()
    cart.product_id = id
    if str(way) == '+':
        cart.quantity = quantity + 1
    else:
        cart.quantity = quantity - 1
    cart.save()


def add_to_cart(request, id: int):
    edit_cart_product(id, '+')
    return render(request, 'cart.html', context={'cart': Cart.objects.all()})


def delete_from_cart(request, id: int):
    edit_cart_product(id, '-')
    return render(request, 'cart.html', context={'cart': Cart.objects.all()})
