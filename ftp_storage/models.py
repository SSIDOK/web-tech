from django.db import models

class Product_ftp_storage(models.Model):
    SUPPORT_CHOICES = [
        ('email', 'Електронна пошта'),
        ('phone', 'Телефон'),
        ('email_phone', 'Електронна пошта або телефон, чат, елекронна пошта'),
    ]

    SSL_CHOICES = [
        ('yes', 'Так'),
        ('no', 'Ні'),
    ]

    RENT_DURATION_CHOICES = [
        ('1_month', '1 місяць'),
    ]

    name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(null=True)
    support = models.CharField(max_length=50, choices=SUPPORT_CHOICES, blank=True)
    ssl = models.CharField(max_length=3, choices=SSL_CHOICES, blank=True)
    rent_duration = models.CharField(max_length=20, choices=RENT_DURATION_CHOICES, blank=True)

    def __str__(self):
        return self.name

    def get_support_display(self):
        return dict(self.SUPPORT_CHOICES).get(self.support, self.support)

    def get_ssl_display(self):
        return dict(self.SSL_CHOICES).get(self.ssl, self.ssl)

    def get_rent_duration_display(self):
        return dict(self.RENT_DURATION_CHOICES).get(self.rent_duration, self.rent_duration)
