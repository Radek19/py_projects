# Generated by Django 2.2 on 2019-05-29 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_orderitems_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='priceVAT',
        ),
    ]
