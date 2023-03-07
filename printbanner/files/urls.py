from django.contrib import admin
from django.urls import path, include
from .views import index, add, delete

urlpatterns = [
    path('', index, name='home'),
    path('add/', add, name="add"),  # форма добавления файла

    # path('edit/<int:id>/', edit),
    path('delete/<int:id>/', delete),

    # path('files/', FilesCreate.as_view())

]