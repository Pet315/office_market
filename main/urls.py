from django.urls import path
from main.views import *

urlpatterns = [
    path('', category),
    path('products/<int:id>/', product),
    path('cart/', cart)
]