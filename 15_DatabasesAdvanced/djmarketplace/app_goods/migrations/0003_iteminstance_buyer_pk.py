# Generated by Django 3.2.6 on 2021-08-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0002_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminstance',
            name='buyer_pk',
            field=models.IntegerField(default=0, verbose_name='в чьей корзине'),
        ),
    ]
