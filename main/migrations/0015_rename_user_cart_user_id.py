# Generated by Django 4.1.7 on 2023-04-20 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_id',
        ),
    ]