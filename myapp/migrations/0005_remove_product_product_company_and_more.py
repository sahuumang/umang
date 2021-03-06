# Generated by Django 4.0.5 on 2022-06-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_company',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_model',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(default='', upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(default='', upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(default='', upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_material',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_weigth',
            field=models.CharField(default='', max_length=100),
        ),
    ]
