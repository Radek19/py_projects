# Generated by Django 2.2 on 2019-05-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_remove_orderitems_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
            preserve_default=False,
        ),
    ]