from django.contrib import admin
from shop.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'price')


admin.site.register(Product, ProductAdmin)