from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ACTIVITY_CHOICES = [
        (True, 'верифицирован'),
        (False, 'не верифицирован')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, verbose_name='телефон')
    city = models.CharField(max_length=36, blank=True, verbose_name='город')
    verification = models.BooleanField(default=False, choices=ACTIVITY_CHOICES, verbose_name='верификация')
    news_count = models.IntegerField(default=0, verbose_name='количество новостей')
