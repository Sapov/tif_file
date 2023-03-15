from django.contrib import admin
from django.urls import path, include
from .views import index, add, delete, edit, FilesUpdateView, FilesCreateView

app_name = 'files'

urlpatterns = [
    path('', index, name='home'),
    path('add/', add, name="add"),  # форма добавления файла
    path('create/<pk>', FilesUpdateView.as_view(), name="update_files"),  # форма добавления файла
    path('create', FilesCreateView.as_view(), name="Create_files"),  # форма добавления файла

    # path('edit/<int:id>/', edit),
    path('delete/<int:id>/', delete),

    # path('files/', FilesCreate.as_view())

]
