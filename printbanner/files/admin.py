from django.contrib import admin
from .models import Material, Product, Organisation, Contractor, TypePrint


class MaterialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Material._meta.fields]

    class Meta:
        model = Material


admin.site.register(Material, MaterialAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Organisation)
admin.site.register(Contractor)


class TypePrintAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TypePrint._meta.fields]

    class Meta:
        model = TypePrint


admin.site.register(TypePrint, TypePrintAdmin)
