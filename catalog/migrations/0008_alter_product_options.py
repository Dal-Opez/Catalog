# Generated by Django 5.2 on 2025-05-09 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_unpublish_product', 'Can unpublish product'), ('can_delete_product', 'Can delete product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
