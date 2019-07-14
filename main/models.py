from django.db import models
from datetime import datetime


class ItemCategory(models.Model):
    item_category = models.CharField('Kategoria', max_length=200)
    category_summary = models.CharField('Opis kategorii', max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.item_category


class ItemSeries(models.Model):
    item_series = models.CharField('Seria', max_length=200)
    item_category = models.ForeignKey(ItemCategory,
                                      default=1,
                                      verbose_name="Kategoria",
                                      on_delete=models.CASCADE)
    series_summary = models.CharField('Opis serii', max_length=200)

    class Meta:
        verbose_name_plural = "Serie"

    def __str__(self):
        return self.item_series


class Item(models.Model):
    item_title = models.CharField('Tytuł obiektu', max_length=200)
    item_content = models.TextField('Treść obiektu')
    item_published = models.DateTimeField('Opublikowano', default=datetime.now)
    item_series = models.ForeignKey(ItemSeries,
                                    default=1,
                                    verbose_name="Seria",
                                    on_delete=models.CASCADE)
    item_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Obiekty"

    def __str__(self):
        return self.item_title
