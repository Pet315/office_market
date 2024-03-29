from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)
    examples = models.TextField(max_length=470, null=True)
    # photo = models.ImageField(upload_to='categories/')
    # is_visible = models.BooleanField(default=True)

    # def __iter__(self):
    #     for product in self.products.all():
    #         yield product

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(max_length=470)
    # photo = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=470)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product}'
