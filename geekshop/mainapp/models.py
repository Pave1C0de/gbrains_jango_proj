from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='название', unique=True)
    description = models.TextField(verbose_name='описание')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    def __str__(self):
        return f'#{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', )

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=128, verbose_name='название', unique=True)
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='изображение')
    short_desc = models.CharField(max_length=128, verbose_name='краткое описание')
    description = models.TextField(max_length=128, verbose_name=' полное описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    quantity =models.PositiveSmallIntegerField(default=0, verbose_name='количество')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'