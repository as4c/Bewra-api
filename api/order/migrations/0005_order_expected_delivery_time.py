# Generated by Django 5.0 on 2024-02-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_total_items_order_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expected_delivery_time',
            field=models.CharField(choices=[('15MN', '15 Minute'), ('30MN', '30 Minute'), ('45MN', '45 Minute'), ('1H', '1 Hours'), ('3H', '3 Hours'), ('6H', '6 Hours'), ('9H', '9 Hours'), ('12H', '12 Hours'), ('1d', '1 Day'), ('7d', '7 Day'), ('1M', '1 Month')], default='1H', max_length=4),
        ),
    ]
