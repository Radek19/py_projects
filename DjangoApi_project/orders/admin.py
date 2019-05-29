from django.contrib import admin
from . models import Order, OrderItems
from shop.models import Product


# admin.site.register(Order)


# admin.site.register(OrderItems)


class OrderItemsInline(admin.TabularInline):
    model = OrderItems


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [OrderItemsInline, ]
