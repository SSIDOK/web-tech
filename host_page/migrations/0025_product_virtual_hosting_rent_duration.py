# Generated by Django 5.0.1 on 2024-05-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_page', '0024_product_virtual_hosting_ssl'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_virtual_hosting',
            name='rent_duration',
            field=models.CharField(blank=True, choices=[('1_month', '1 місяць')], max_length=20),
        ),
    ]