# Generated by Django 5.0 on 2023-12-26 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_status_paymentbyuser_payment_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentbyuser',
            name='quantity',
        ),
    ]