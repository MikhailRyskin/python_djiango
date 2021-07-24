from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='заголовок')
    description = models.TextField(max_length=1500, default='', verbose_name='объявление')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               verbose_name='автор', related_name='advertisements')
    rubric = models.ForeignKey('AdvertisementRubric', default=None, null=True, on_delete=models.CASCADE,
                               verbose_name='рубрика', related_name='advertisements')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AdvertisementRubric(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
