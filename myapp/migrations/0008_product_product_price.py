# Generated by Django 4.0.5 on 2022-06-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_product_weigth_product_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='', max_length=100),
        ),
    ]