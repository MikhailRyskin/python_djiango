# Generated by Django 2.2 on 2021-07-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='what_news',
            new_name='what_new',
        ),
    ]
