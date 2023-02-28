from django.shortcuts import render
from .models import Files


# def home_page(request):
#     # получаем все значения модели
#     data = Files.objects.all()
#     return render(request, 'home_page.html', {'data': data})

from django.core.files.storage import FileSystemStorage

def home_page(request):
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        Files.objects.create(title='some title', cover=request.FILES['myfile1'])

        return render(request, 'home_page.html', {
            'file_url': file_url
        })
    return render(request, 'home_page.html')