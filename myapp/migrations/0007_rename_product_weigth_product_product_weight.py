# Generated by Django 4.0.5 on 2022-06-04 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_weigth',
            new_name='product_weight',
        ),
    ]
