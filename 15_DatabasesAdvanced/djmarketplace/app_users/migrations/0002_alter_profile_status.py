# Generated by Django 3.2.6 on 2021-08-31 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, default='обычный', max_length=20, verbose_name='статус'),
        ),
    ]