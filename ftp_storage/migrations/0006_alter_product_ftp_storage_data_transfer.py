# Generated by Django 5.0.1 on 2024-05-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp_storage', '0005_alter_product_ftp_storage_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_ftp_storage',
            name='data_transfer',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]