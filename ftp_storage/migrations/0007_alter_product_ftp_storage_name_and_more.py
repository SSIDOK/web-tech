# Generated by Django 5.0.1 on 2024-05-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftp_storage', '0006_alter_product_ftp_storage_data_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_ftp_storage',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product_ftp_storage',
            name='ssl',
            field=models.CharField(blank=True, choices=[('yes', 'Так'), ('no', 'Ні')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product_ftp_storage',
            name='support',
            field=models.CharField(blank=True, choices=[('email', 'Електронна пошта'), ('phone', 'Телефон'), ('email_phone', 'Електронна пошта або 24/7 телефон, чат, елекронна пошта')], max_length=50),
        ),
    ]