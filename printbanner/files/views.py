from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Product
from .forms import UploadFiles

from django.core.files.storage import FileSystemStorage


def index(request):
    product = Product.objects.all()
    return render(request, "index.html", {"product": product, 'title': 'Загрузка файлов'})


def create(request):
    if request.method == "POST":
        product = Product()

        # product.quantity = request.POST.get('quantity')
        # product.width = request.POST.get('width')
        # product.length = request.POST.get('length')
        product.path_file = request.POST.get('images')
        product.save()


        return HttpResponseRedirect("/")


def add(request):
    if request.POST:
        form = UploadFiles(request.POST, request.FILES)
        print(request.FILES['images'])
        if form.is_valid():
            # file_name_add(request.FILES['path_file'])

            form.save()

            return HttpResponseRedirect("/")
    else:
        form = UploadFiles

    return render(request, 'add.html',
                  {'form': form, 'title': 'Добавление файлов'})  # изменение данных в БД


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
