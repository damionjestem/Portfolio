from django.contrib import admin
from django.db import models
from .models import Item, ItemSeries, ItemCategory
from tinymce.widgets import TinyMCE


# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['item_title', 'item_published']}),
        ('URL', {'fields': ['item_slug']}),
        ('Series', {'fields': ['item_series']}),
        ('Content', {'fields': ['item_content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


admin.site.register(ItemSeries)
admin.site.register(ItemCategory)
admin.site.register(Item, ItemAdmin)
