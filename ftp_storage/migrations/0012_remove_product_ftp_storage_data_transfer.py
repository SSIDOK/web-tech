# Generated by Django 5.0.1 on 2024-05-14 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftp_storage', '0011_product_ftp_storage_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_ftp_storage',
            name='data_transfer',
        ),
    ]
