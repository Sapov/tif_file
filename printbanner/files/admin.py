from django.contrib import admin
from .models import Material, Product, Organisation, Contractor, Orders

admin.site.register(Material)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(Organisation)
admin.site.register(Contractor)

