# Generated by Django 4.1.7 on 2023-04-20 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]