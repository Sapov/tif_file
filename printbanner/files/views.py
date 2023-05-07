from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product, Material
from .forms import UploadFiles
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin  # new


# from django.core.files.storage import FileSystemStorage
@login_required
def index(request):
    '''Вывод файлов толоко авторизованного пользователя'''
    product = Product.objects.filter(Contractor=request.user)

    return render(request, "index.html", {"product": product, 'title': 'Загрузка файлов'})


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


class FilesUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ("__all__")
    template_name = 'product_update_form.html'
    login_url = 'login'


class FilesCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['quantity', 'material', 'images']

    def form_valid(self, form):
        form.instance.Contractor = self.request.user
        return super().form_valid(form)


def price(request):
    price = Material.objects.filter(type_print=1)  # Только широкоформатная печать!!!
    # price = Material.objects.all()
    return render(request, "price.html", {"price": price, 'title': 'sdsdsdf'})


class FileList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'index_detail.html'
    login_url = 'login'



