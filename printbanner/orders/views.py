from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Order


class OrderCreateView(CreateView):
    model = Order
    # fields = ['Contractor','quantity', 'material', 'images']
    fields = ("__all__")
