# Generated by Django 2.2 on 2019-05-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20190528_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
