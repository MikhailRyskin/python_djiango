# Generated by Django 2.2 on 2021-07-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_auto_20210726_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='activity',
            field=models.BooleanField(default=True, verbose_name='активность'),
        ),
        migrations.AlterField(
            model_name='new',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата публикации'),
        ),
    ]
