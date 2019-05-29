from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    priceVAT = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name
