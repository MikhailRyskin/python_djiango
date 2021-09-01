# Generated by Django 3.2.6 on 2021-09-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_profile_amount_purchases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='amount_purchases',
            field=models.FloatField(blank=True, default=0, verbose_name='сумма покупок'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(blank=True, default=0, verbose_name='баланс'),
        ),
    ]