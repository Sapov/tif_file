from django.db import models


# class Files(models.Model):
#     title = models.CharField(max_length=150)
#     cover = models.ImageField(upload_to='images/')
#     # book = models.FileField(upload_to='books/')


class Material(models.Model):
    name = models.CharField(max_length=100, help_text='Введите имя материала для печати',
                            verbose_name='Материал для печати', blank=True, null=True, default=None)
    price = models.FloatField(max_length=100, help_text='Стоимость печати в руб.', verbose_name='За 1 метр квадратный')
    resolution_print = models.IntegerField(help_text='разрешение для печати на материале', verbose_name='DPI',
                                           blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    COLOR_MODE = (
        ('RGB', 'rgb'),
        ('CMYK', 'cmyk'),
        ('GREY', 'Greyscale'),
        ('LAB', 'lab')
    )

    name = models.CharField(max_length=60, verbose_name='Имя файла')
    # order = models.ForeignKey('Orders', on_delete=models.CASCADE, verbose_name='order')
    material = models.ForeignKey("Material", on_delete=models.CASCADE, verbose_name='Материал')
    # order = models.ForeignKey('Orders', on_delete=models.CASCADE, verbose_name='Заказы')
    quantity = models.IntegerField(default=1, help_text='Введите количество', verbose_name="Количество")
    width = models.FloatField(default=0, verbose_name="Ширина", help_text="Указывается в см.")
    length = models.FloatField(default=0, verbose_name="Длина", help_text="Указывается в см.")
    resolution = models.IntegerField(default=0, verbose_name="Разрешение",
                                     help_text="для баннера 72 dpi, для Пленки 150 dpi")
    color_model = models.CharField(max_length=10, choices=COLOR_MODE, verbose_name="Цветовая модель",
                                   help_text="Для корректной печати модель должна быть CMYK")
    size = models.FloatField(default=0, verbose_name="Размер в Мб")
    # price = models.FloatFeld(default=0, verbose_name="Стоимость")
    images = models.ImageField(upload_to='image/%d_%m_%y')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update
    # objects = models.Manager()
    # DoesNotExist = models.Manager

    #
    def __str__(self):
        return f'{self.id}-{self.material}'