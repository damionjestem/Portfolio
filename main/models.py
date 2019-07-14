from django.db import models
from datetime import datetime


class Item(models.Model):
    item_title = models.CharField('Tytuł obiektu', max_length=200)
    item_content = models.TextField('Treść obiektu')
    item_published = models.DateTimeField('Opublikowano', default=datetime.now)

    def __str__(self):
        return self.item_title
