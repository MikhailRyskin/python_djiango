from django.db import models


class Shop(models.Model):
    """Модель магазина"""
    name = models.CharField(max_length=200, verbose_name='название')

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    """Модель товара"""
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='магазин')
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, verbose_name='цена')
    number_on_sale = models.PositiveIntegerField(blank=True, default=0, verbose_name='количество в продаже')
    number_of_sold = models.PositiveIntegerField(blank=True, default=0, verbose_name='количество проданных')

    def __str__(self):
        return f'{self.name} артикул: {self.pk}'


class ItemInstance(models.Model):
    """Модель экземпляра товара"""
    item = models.ForeignKey(Item, related_name='instances', on_delete=models.CASCADE, verbose_name='товар')
    buyer_pk = models.IntegerField(default=0, verbose_name='в чьей корзине')
    status = models.CharField(max_length=20,  blank=True, default='в продаже', verbose_name='статус')
    date_of_sale = models.DateField(blank=True, null=True)
