from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    title = models.CharField(max_length=100, verbose_name='заглавие')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='категория')

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    text = models.TextField(verbose_name='текст')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, verbose_name='продукт')

    def __str__(self):
        return self.text
