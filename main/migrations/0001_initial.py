# Generated by Django 3.1.7 on 2021-03-29 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категории')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование продукта')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена продукта')),
                ('photo', models.ImageField(null=True, upload_to='prod_photos')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('marka', models.CharField(max_length=255, verbose_name='Модель продукта')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='main.tagcategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('price',),
            },
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема')),
                ('review', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв клиента',
                'verbose_name_plural': 'Отзывы клиентов',
                'ordering': ('pub_date',),
            },
        ),
    ]
