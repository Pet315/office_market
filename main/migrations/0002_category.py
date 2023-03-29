# Generated by Django 4.1.7 on 2023-03-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
