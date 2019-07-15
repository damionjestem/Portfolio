# Generated by Django 2.2.2 on 2019-07-14 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190714_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Obiekty'},
        ),
        migrations.AlterModelOptions(
            name='itemseries',
            options={'verbose_name_plural': 'Serie'},
        ),
        migrations.AlterField(
            model_name='item',
            name='item_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.ItemSeries', verbose_name='Seria'),
        ),
        migrations.AlterField(
            model_name='itemseries',
            name='item_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.ItemCategory', verbose_name='Kategoria'),
        ),
    ]