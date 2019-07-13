from django.db import models


class Item(models.Model):
    item_title = models.CharField('Tytuł obiektu', max_length=200)
    item_content = models.TextField('Treść obiektu')
    item_publisher = models.DateTimeField('Opublikowano')

    def __str__(self):
        return self.item_title
