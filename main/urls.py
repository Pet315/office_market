from django.urls import path
from main.views import *

urlpatterns = [
    path('', category),
    path('products/<int:id>/', product),
    path('cart/', cart),
    path('cart/<int:id>/', add_to_cart),
    path('cart/delete_product/<int:id>/', delete_from_cart)
]