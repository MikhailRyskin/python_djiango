# Generated by Django 2.2 on 2021-08-01 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0007_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='', max_length=100, verbose_name='текст комментария'),
        ),
    ]
