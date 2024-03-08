# Generated by Django 5.0 on 2024-02-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('A', 'Accepted'), ('P', 'Packed'), ('F', 'Failed'), ('C', 'Cancell'), ('R', 'Return'), ('D', 'Delivered'), ('O', 'On the way')], default='P', max_length=1),
        ),
    ]