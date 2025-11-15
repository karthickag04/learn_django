from django.contrib import admin
from .models import ProductAll

# Register your models here.

@admin.register(ProductAll)
class ProductAllAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'stock', 'is_active','description', 'image', 'image_url')
    list_filter = ('is_active',)
    search_fields = ('product_name','product_price')