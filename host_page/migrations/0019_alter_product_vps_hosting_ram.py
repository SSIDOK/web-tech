# Generated by Django 5.0.1 on 2024-05-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_page', '0018_alter_product_vps_hosting_databases_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_vps_hosting',
            name='ram',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
