from django.contrib import admin
from django.urls import path, include
from .views import index, delete, FilesUpdateView, FilesCreateView, price

app_name = 'files'

urlpatterns = [
    path('', index, name='home'),
    path('create/', FilesCreateView.as_view(), name="create_files"),  # форма добавления файла
    path('create/<pk>', FilesUpdateView.as_view(), name="update_files"),  # форма добавления файла

    path('delete/<int:id>/', delete),
    path('price/', price),

    # path('files/', FilesCreate.as_view())

]
