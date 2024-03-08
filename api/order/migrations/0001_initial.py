# Generated by Django 5.0 on 2023-12-25 11:45

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_items', models.IntegerField(default=1)),
                ('total_actual_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_effective_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_discount_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('order_status', models.CharField(choices=[('A', 'Accepted'), ('P', 'Pending'), ('F', 'Failed'), ('C', 'Cancel'), ('R', 'Return'), ('D', 'Delivered')], default='P', max_length=1)),
                ('payment_mode', models.CharField(choices=[('COD', 'Cash On Delivery'), ('ONL', 'Online')], max_length=3)),
                ('payment_status', models.CharField(choices=[('S', 'Success'), ('F', 'Failed'), ('P', 'Pending')], default='P', max_length=1)),
                ('transaction_id', models.CharField(default='003jkdkkdkdk', max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('customer_address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.address')),
                ('products', models.ManyToManyField(blank=True, related_name='ordered_items', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
