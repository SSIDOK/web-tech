# Generated by Django 5.0.1 on 2024-05-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp_storage', '0012_remove_product_ftp_storage_data_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_ftp_storage',
            name='support',
            field=models.CharField(choices=[('email', 'Електронна пошта'), ('phone', 'Телефон'), ('email_phone', 'Електронна пошта або телефон, чат, елекронна пошта')], max_length=50),
        ),
    ]
