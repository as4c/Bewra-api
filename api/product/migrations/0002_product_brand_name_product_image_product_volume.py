# Generated by Django 5.0 on 2024-01-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
