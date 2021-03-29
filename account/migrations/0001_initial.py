# Generated by Django 3.1.7 on 2021-03-21 18:37

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
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия пользователя')),
                ('photo', models.ImageField(null=True, upload_to='account_photos/Y%/%m/%d/', verbose_name='Аватар пользователя')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Телефон пользователя')),
                ('regis_at', models.DateTimeField(auto_now=True, verbose_name='Дата регистрации')),
                ('biography', models.TextField(verbose_name='О себе')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('-regis_at',),
            },
        ),
    ]
