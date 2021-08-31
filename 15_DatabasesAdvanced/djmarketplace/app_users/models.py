from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(blank=True, default=0, verbose_name='баланс')
    amount_purchases = models.PositiveIntegerField(blank=True, default=0, verbose_name='баланс')
    status = models.CharField(max_length=20,  blank=True, default='обычный', verbose_name='статус')
