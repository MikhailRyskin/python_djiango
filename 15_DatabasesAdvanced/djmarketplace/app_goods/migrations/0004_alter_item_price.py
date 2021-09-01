# Generated by Django 3.2.6 on 2021-09-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0003_iteminstance_buyer_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='цена'),
        ),
    ]