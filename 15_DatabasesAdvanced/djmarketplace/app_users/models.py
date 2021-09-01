from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Модель профиля пользователя, дополняющая User Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, verbose_name='баланс')
    amount_purchases = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0,
                                           verbose_name='сумма покупок')
    status = models.CharField(max_length=20,  blank=True, default='обычный', verbose_name='статус')
