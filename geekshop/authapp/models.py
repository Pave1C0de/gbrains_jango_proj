from django.db import models


from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='', blank=True, verbose_name='Аватарка')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
