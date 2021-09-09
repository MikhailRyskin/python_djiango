from django.db import models


class RoomsQuantity(models.Model):
    quantity = models.CharField(max_length=64, verbose_name='количество комнат')

    class Meta:
        verbose_name = 'количество комнат'
        verbose_name_plural = 'количества комнат'

    def __str__(self):
        return self.quantity


class HousingType(models.Model):
    type = models.CharField(max_length=64, verbose_name='тип жилья')

    class Meta:
        verbose_name = 'тип жилья'
        verbose_name_plural = 'типы жилья'

    def __str__(self):
        return self.type


class Housing(models.Model):
    title = models.CharField(max_length=256, verbose_name='название жилья')
    description = models.TextField(verbose_name='описание жилья')
    price = models.PositiveIntegerField(verbose_name='цена жилья')
    type = models.ForeignKey(HousingType, on_delete=models.SET_NULL, related_name='types',
                             null=True, verbose_name='тип жилья')
    rooms_quantity = models.ForeignKey(RoomsQuantity, on_delete=models.SET_NULL, related_name='numbers',
                                       null=True, verbose_name='количество комнат')

    class Meta:
        verbose_name = 'жилище'
        verbose_name_plural = 'жилища'

    def __str__(self):
        return self.title
