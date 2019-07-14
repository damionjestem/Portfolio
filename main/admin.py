from django.contrib import admin
from django.db import models
from .models import Item
from tinymce.widgets import TinyMCE


# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['item_title', 'item_published']}),
        ('Content', {'fields': ['item_content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Item, ItemAdmin)
