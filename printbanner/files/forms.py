from .models import Product
from django.forms import ModelForm

from django import forms
from .models import *


class UploadFiles(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['material', "quantity", 'width', 'length', 'images']


class UpdateFiles(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['material', "quantity", 'width', 'length', 'images']
