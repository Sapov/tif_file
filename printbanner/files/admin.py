from django.contrib import admin
from .models import Material, Product, Organisation, Contractor, TypePrint

admin.site.register(Material)
admin.site.register(Product)
admin.site.register(Organisation)
admin.site.register(Contractor)
admin.site.register(TypePrint)


