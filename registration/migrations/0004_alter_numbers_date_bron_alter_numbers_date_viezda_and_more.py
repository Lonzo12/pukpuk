# Generated by Django 4.2.6 on 2023-10-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_numbers_date_bron_alter_numbers_date_viezda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numbers',
            name='date_bron',
            field=models.DateField(blank='True', verbose_name='Дата бронирования'),
        ),
        migrations.AlterField(
            model_name='numbers',
            name='date_viezda',
            field=models.DateField(blank='True', verbose_name='Дата выезда'),
        ),
        migrations.AlterField(
            model_name='numbers',
            name='date_zaezda',
            field=models.DateField(blank='True', verbose_name='Дата заезда'),
        ),
    ]