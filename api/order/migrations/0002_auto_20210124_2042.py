# Generated by Django 3.0.8 on 2021-01-24 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product_name',
            new_name='product_names',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='total_product',
            new_name='total_products',
        ),
    ]
