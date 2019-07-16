from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, ItemSeries, ItemCategory

# Create your views here.


def homepage(request):
    return render(request,
                  "main/categories.html",
                  {"categories": ItemCategory.objects.all})


def single_slug(request, single_slug):
    categories = [c.category_slug for c in ItemCategory.objects.all()]
    if single_slug in categories:
        matching_series = ItemSeries.objects.filter(item_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            first = Item.objects.filter(item_series__item_series=m.item_series).earliest("item_published")
            series_urls[m] = first.item_slug

        return render(request,
                      "main/category.html",
                      context={"firsts": series_urls})

    items = [i.item_slug for i in Item.objects.all()]
    if single_slug in items:
        return HttpResponse(f"{single_slug} to obiekt")

    return HttpResponse(f"{single_slug} nie odpowiada niczemu")
