# Generated by Django 5.0 on 2024-03-04 08:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
