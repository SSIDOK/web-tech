# Generated by Django 5.0.1 on 2024-05-13 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_page', '0011_rename_product_vps_hosting_product_web_hosting'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_web_hosting',
        ),
    ]
