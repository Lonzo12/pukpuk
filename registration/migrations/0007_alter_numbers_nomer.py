# Generated by Django 4.2.6 on 2023-10-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_numbers_date_bron_alter_numbers_date_viezda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numbers',
            name='nomer',
            field=models.IntegerField(verbose_name='Номер'),
        ),
    ]
