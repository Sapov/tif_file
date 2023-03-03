from django.shortcuts import render
from .models import Product

from django.core.files.storage import FileSystemStorage


def index(request):
    product = Product.objects.all()
    return render(request, "index.html", {"product": product, 'title': 'Загрузка файлов'})
