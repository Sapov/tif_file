from django.db import models
from files.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return 'Cтатус %s' % self.name


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for all products

    customer_name = models.CharField(max_length=20)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=24, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

    def __str__(self):
        return 'Cтатус %s %s' % (self.id, self.status.name)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1, verbose_name="Кол-во")
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Стоимость 1 Ед.")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price * nmb
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name_plural = 'Товары в заказе'
        verbose_name = 'Товар в заказе'

    def __str__(self):
        return str(self.product.images)

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for items in all_products_in_order:
        order_total_price += items.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_order_post_save, sender=ProductInOrder)
