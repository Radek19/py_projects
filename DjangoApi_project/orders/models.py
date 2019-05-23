from django.db import models
from shop.models import Product


class Order(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    priceVAT = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('-order_date',)

    def __str__(self):
        return 'Order {}'.format(self.id)
