from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                    related_name='profile', verbose_name='Пользователь')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='account_photos', null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон')
    regis_at = models.DateTimeField(auto_now=True, verbose_name='Дата регистрации')
    biography = models.TextField(verbose_name='О себе')

    def __str__(self):
        return f"{self.user} - {self.first_name}"

    class Meta:
        ordering = ('-regis_at',)
        verbose_name = 'Профиль клиента'
        verbose_name_plural = 'Профили клиентов'


