# Generated by Django 5.0 on 2024-02-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryboy', '0004_deliveryboy_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboy',
            name='orders',
        ),
    ]
