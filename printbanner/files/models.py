from django.db import models
from django.urls import reverse

# from img_file.img_tif import check_tiff
from .tiff_file import check_tiff


class Contractor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Поставщик продукции')

    class Meta:
        verbose_name_plural = 'Подрядчики'
        verbose_name = 'Подрядчик'
        ordering = ['name']

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name_ul = models.CharField(max_length=70, verbose_name="Имя юр. лица", help_text='Форма собственности и название')
    address_ur = models.TextField(null=True, blank=True, verbose_name='Юр. Адрес', help_text="Полный почтовый адрес")
    address_post = models.TextField(null=True, blank=True, verbose_name='Почтовый Адрес')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    email = models.EmailField(max_length=20, blank=True, verbose_name='Электронная почта')
    inn = models.CharField(max_length=12, verbose_name='ИНН', blank=True)
    kpp = models.CharField(max_length=9, verbose_name='КПП', blank=True)
    okpo = models.CharField(max_length=12, blank=True, verbose_name='ОКПО')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Организации'
        verbose_name = 'Организация'
        ordering = ['name_ul']

    def __str__(self):
        return self.name_ul


class TypePrint(models.Model):
    type_print = models.CharField(max_length=128, verbose_name='Метод печати')
    info_type_print = models.TextField()

    class Meta:
        verbose_name_plural = 'Типы печати'
        verbose_name = 'Тип печати'
        ordering = ['type_print']

    def __str__(self):
        return self.type_print


class Material(models.Model):
    name = models.CharField(max_length=100, help_text='Введите имя материала для печати',
                            verbose_name='Материал для печати', blank=True, null=True, default=None)
    type_print = models.ForeignKey(TypePrint, on_delete=models.CASCADE, verbose_name='Тип печати', blank=True,
                                   null=True, default=None)
    price_contractor = models.FloatField(max_length=100, help_text='За 1 м2',
                                         verbose_name='Себестоимость печати в руб.', blank=True, null=True,
                                         default=None)  # стоимость в закупке
    price = models.FloatField(max_length=100, help_text='За 1 м2', verbose_name='Стоимость печати в руб.')
    resolution_print = models.IntegerField(help_text='разрешение для печати на материале', verbose_name='DPI',
                                           blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Материалы для печати'
        verbose_name = 'Материал'
        ordering = ['name']


class Product(models.Model):
    COLOR_MODE = (
        ('RGB', 'rgb'),
        ('CMYK', 'cmyk'),
        ('GREY', 'Greyscale'),
        ('LAB', 'lab')
    )
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    Contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, verbose_name='ЗАКАЗЧИК!!')
    material = models.ForeignKey("Material", on_delete=models.CASCADE, verbose_name='Материал')
    quantity = models.IntegerField(default=1, help_text='Введите количество', verbose_name="Количество")
    width = models.FloatField(default=0, verbose_name="Ширина", help_text="Указывается в см.")
    length = models.FloatField(default=0, verbose_name="Длина", help_text="Указывается в см.")
    resolution = models.IntegerField(default=0, verbose_name="Разрешение",
                                     help_text="для баннера 72 dpi, для Пленки 150 dpi")
    color_model = models.CharField(max_length=10, choices=COLOR_MODE, verbose_name="Цветовая модель",
                                   help_text="Для корректной печати модель должна быть CMYK")
    size = models.FloatField(default=0, verbose_name="Размер в Мб")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    images = models.FileField(upload_to='image/%d_%m_%y')
    preview_images = models.FileField(upload_to='image/%d_%m_%y', blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    # objects = models.Manager()
    # DoesNotExist = models.Manager

    #
    def __str__(self):
        return f'{self.id}-{self.material}'

    def get_absolute_url(self):
        return reverse('files:home')
        # return reverse('files:update_files', args=[self.id])

    class Meta:
        verbose_name_plural = 'Файлы'
        verbose_name = 'Файл'
        # ordering = ['name']

    def save(self, *args, **kwargs):
        ''' расчет и запись стоимость баннера'''
        # check type file
        # calculation
        # preview
        self.width, self.length, self.resolution = check_tiff(self.images) # Читаем размеры из Tiff
        price_per_item = self.material.price
        self.price = (self.width) / 100 * (self.length) / 100 * self.quantity * price_per_item
        super(Product, self).save(*args, **kwargs)

