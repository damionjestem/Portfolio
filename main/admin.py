from django.contrib import admin
from .models import Item

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['item_title', 'item_published']}),
        ('Content', {'fields': ['item_content']})
    ]


admin.site.register(Item)
