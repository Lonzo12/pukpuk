# Generated by Django 4.2.6 on 2023-11-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_products_pict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pict',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
