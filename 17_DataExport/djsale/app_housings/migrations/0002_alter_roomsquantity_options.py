# Generated by Django 3.2.6 on 2021-09-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_housings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomsquantity',
            options={'verbose_name': 'количество комнат', 'verbose_name_plural': 'количества комнат'},
        ),
    ]
