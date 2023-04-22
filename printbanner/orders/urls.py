from django.urls import path
from .views import OrderCreateView

app_name = 'orders'

urlpatterns = [
    # path('', index, name='home'),
    path('', OrderCreateView.as_view(), name="create_orders"),  # форма добавления файла
]




