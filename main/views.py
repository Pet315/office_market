from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from main.models import Product, Category, Cart


def category(request):
    categories = Category.objects.all()
    user_profile = request.user
    return render(request, 'categories.html', context={'categories': categories, 'user_profile': user_profile})


def product(request, id: int):
    if id > len(Category.objects.all()):
        return HttpResponseNotFound('Wrong number')
    user_profile = request.user
    products = Product.objects.filter(category_id=id)
    return render(request, 'products.html', context={'products': products, 'user_profile': user_profile})


def cart(request):
    user_profile = request.user
    return render(request, 'cart.html', context={'user_profile': user_profile})


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
