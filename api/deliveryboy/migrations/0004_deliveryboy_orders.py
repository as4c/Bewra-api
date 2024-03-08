# Generated by Django 5.0 on 2024-02-29 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryboy', '0003_deliveryboy_curr_parcel_cnt'),
        ('order', '0008_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
    ]
