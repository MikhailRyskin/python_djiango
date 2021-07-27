from django.db import models


class New(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='название')
    content = models.TextField(max_length=20000, default='', verbose_name='содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activity = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    what_new = models.ForeignKey('New', default=None, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, verbose_name='имя пользователя')
    text = models.TextField(max_length=1000, default='', verbose_name='текст комментария')

    def __str__(self):
        return self.user_name
