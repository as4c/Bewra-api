# Generated by Django 5.0 on 2024-02-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryboy', '0002_remove_deliveryboy_area_deliveryboy_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='curr_parcel_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
