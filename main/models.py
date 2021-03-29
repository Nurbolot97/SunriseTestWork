from django.db import models
from django.contrib.auth.models import User

from account.models import UserAccount



class Product(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование продукта')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена продукта')
    photo = models.ImageField(upload_to="prod_photos", null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание', null=True)
    marka = models.CharField(max_length=255, verbose_name='Модель продукта')
    category = models.ForeignKey('TagCategory', on_delete=models.CASCADE, null=True, related_name='product_category')
    

    def __str__(self):
        return f"{self.title} - {self.slug}"

    class Meta:
        ordering = ('price',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class TagCategory(models.Model):

    title = models.CharField(verbose_name='Категории', max_length=255)
    slug = models.SlugField(unique=True, null=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.title}"


class CustomerReview(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_review')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    review = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.first_name} - {self.subject}"

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Отзыв клиента'
        verbose_name_plural = 'Отзывы клиентов'
    

