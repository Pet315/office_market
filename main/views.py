from django.http import HttpResponseNotFound
from django.shortcuts import render
from main.models import Product, Category, Cart, Order


def category(request):
    categories = Category.objects.all()
    user_profile = request.user
    # print(request.user.id)
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


def edit_cart_product(product_id, way, user_id):
    if product_id > len(Product.objects.filter()):
        return HttpResponseNotFound('Wrong number')

    product = Cart.objects.filter(product_id=product_id, user_id=user_id)

    if len(product) == 0:
        quantity = 0
    else:
        quantity = product[0].quantity
    product.delete()

    cart = Cart()
    cart.product_id = product_id
    if str(way) == '+':
        cart.quantity = quantity + 1
    else:
        cart.quantity = quantity - 1
    cart.user_id = user_id
    cart.save()


def add_to_cart(request, id: int):
    edit_cart_product(id, '+', request.user.id)
    return render(request, 'cart.html', context={'cart': Cart.objects.all()})


def delete_from_cart(request, id: int):
    edit_cart_product(id, '-', request.user.id)
    return render(request, 'cart.html', context={'cart': Cart.objects.all()})


def send_order(request):
    orders = Cart.objects.filter(user_id=request.user.id)
    print(orders)
    for ord in orders:
        order = Order()
        order.product_id, order.quantity, order.user_id, order.email = ord.product_id, ord.quantity, \
                                                                       ord.user_id, request.POST.get('email')
        order.save()
        ord.delete()
    return render(request, 'order.html')
