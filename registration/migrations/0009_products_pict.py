# Generated by Django 4.2.6 on 2023-11-08 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pict',
            field=models.ImageField(null='выберите фото', upload_to='', verbose_name='Фотография товара'),
            preserve_default='выберите фото',
        ),
    ]
