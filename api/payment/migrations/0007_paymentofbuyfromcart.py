# Generated by Django 5.0 on 2024-02-24 15:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_total_items_order_quantity_and_more'),
        ('payment', '0006_remove_paymentbyuser_payment_mode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentOfBuyFromCart',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('orders', models.ManyToManyField(to='order.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]