from django.contrib import admin
from .models import Category, Product, Customer, CartItem, Order
from .models import Review
import csv
from django.http import HttpResponse


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('category', 'is_active')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'payment_status', 'created_at')
    list_filter = ('payment_status',)
    actions = ['export_orders_csv']

    def export_orders_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        writer = csv.writer(response)
        writer.writerow(['Order ID', 'User', 'Amount', 'Status', 'Date'])
        for order in queryset:
            writer.writerow([order.id, order.user, order.total_amount, order.payment_status, order.created_at])
        return response

    export_orders_csv.short_description = "Export Selected Orders as CSV"