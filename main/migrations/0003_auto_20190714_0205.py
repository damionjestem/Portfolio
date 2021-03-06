# Generated by Django 2.2.2 on 2019-07-14 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190714_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_content',
            field=models.TextField(verbose_name='Treść obiektu'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_publisher',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Opublikowano'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_title',
            field=models.CharField(max_length=200, verbose_name='Tytuł obiektu'),
        ),
    ]
