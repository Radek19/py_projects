from django.contrib import admin
from . models import Order, OrderItems


# admin.site.register(Order)

# admin.site.register(OrderItems)


class OrderItemsInline(admin.TabularInline):
    model = OrderItems


class OrderAdmin(admin.ModelAdmin):

    inlines = [OrderItemsInline, ]


admin.site.register(Order, OrderAdmin)
