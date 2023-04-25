import os

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Product, Material
from .forms import UploadFiles
from django.views.generic.edit import CreateView, UpdateView


# from django.core.files.storage import FileSystemStorage


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
        # os.remove(f'media/{str(product.images)}')

        print(f'media/{str(product.images)}')

        print('Удален ID', id, product.images)

        # os.remove(str(product.preview_images))
        # print('Удален preview ID', id, product.preview_images)

        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.POST:
            product.quantity = request.POST.get("quantity")
            product.width = request.POST.get("width")
            product.length = request.POST.get("length")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html",
                          {"product": product, 'title': 'Редактрирование файлов'})

    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


class FilesUpdateView(UpdateView):
    model = Product
    fields = ("__all__")
    template_name = 'product_update_form.html'
    # template_name_suffix = '_update_form'


class FilesCreateView(CreateView):
    model = Product
    fields = ['Contractor', 'quantity', 'material', 'images']
    # fields = ("__all__")


def price(request):
    price = Material.objects.all()
    return render(request, "price.html", {"price": price, 'title': 'sdsdsdf'})
