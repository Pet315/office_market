# Generated by Django 4.1.7 on 2023-04-20 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_quality_cart_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]