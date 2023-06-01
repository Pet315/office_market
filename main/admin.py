from django.contrib import admin
from main.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'examples']
    list_display_links = ['name', 'examples']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'category']
    list_display_links = ['name', 'category']
    list_filter = ['name', 'price', 'category']
    search_fields = ['name']
    list_per_page = 10


class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'user']
    list_display_links = ['product', 'quantity', 'user']
    list_filter = ['product', 'user']
    search_fields = ['product']
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'user', 'email', 'is_processed']
    list_display_links = ['product', 'quantity', 'user', 'is_processed']
    list_filter = ['product', 'user', 'is_processed']
    search_fields = ['product']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
