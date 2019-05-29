# Generated by Django 2.2 on 2019-05-28 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0009_auto_20190528_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='products',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
            preserve_default=False,
        ),
    ]