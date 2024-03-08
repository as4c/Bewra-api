# Generated by Django 5.0 on 2023-12-25 13:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0003_alter_order_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentByUser',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(choices=[('COD', 'Cash On Delivery'), ('ONL', 'Online')], max_length=3)),
                ('status', models.CharField(choices=[('S', 'Success'), ('F', 'Failed'), ('P', 'Pending')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=500, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]