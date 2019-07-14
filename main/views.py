from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

# Create your views here.


def homepage(request):
    return render(request,
                  "main/home.html",
                  {"items": Item.objects.all})
