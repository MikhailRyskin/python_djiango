from django.db import models
from django.contrib.auth.models import User


class New(models.Model):
    ACTIVITY_CHOICES = [
        (True, 'активна'),
        (False, 'не активна')
    ]

    title = models.CharField(max_length=1000, db_index=True, verbose_name='название')
    content = models.TextField(max_length=20000, default='', verbose_name='содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    activity = models.BooleanField(default=True, choices=ACTIVITY_CHOICES, verbose_name='активность')

    def __str__(self):
        return f'{self.title} {self.created_at} {"активна" if self.activity else "не активна"}'

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    what_new = models.ForeignKey('New', verbose_name='новость',
                                 default=None, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, verbose_name='имя пользователя', blank=True)
    text = models.TextField(max_length=1000, default='', verbose_name='текст комментария')

    def __str__(self):
        return f'{self.user_name} {self.text[:15]}...'
