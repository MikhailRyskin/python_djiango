from django.db import models
from django.urls import reverse


class NewsItem(models.Model):
    title = models.CharField(max_length=128, verbose_name='заголовок новости')
    text = models.TextField(verbose_name='текст новости')
    is_published = models.BooleanField(default=False)
    description = models.TextField(verbose_name='краткое описание новости', default='')
    published_at = models.DateTimeField(verbose_name='дата публикации', null=True)

    def get_absolute_url(self):
        return reverse('newsitem_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
