# Generated by Django 5.0.1 on 2024-05-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_page', '0028_remove_product_virtual_hosting_rent_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_virtual_hosting',
            name='ssl',
            field=models.CharField(choices=[('yes', 'Так'), ('no', 'Ні')], max_length=3),
        ),
    ]
