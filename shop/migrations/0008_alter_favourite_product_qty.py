# Generated by Django 5.1.6 on 2025-03-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_cart_product_qty_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='product_qty',
            field=models.IntegerField(default=1),
        ),
    ]
