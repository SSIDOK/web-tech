from django.db import models


class Product_virtual_hosting(models.Model):

    SSL_CHOICES = [
        ('yes', 'Так'),
        ('no', 'Ні'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    ssd = models.IntegerField()
    websites = models.IntegerField()
    subdomains = models.IntegerField()
    databases = models.IntegerField()
    ram = models.IntegerField()
    ssl = models.CharField(max_length=3, choices=SSL_CHOICES)

    def __str__(self):
        return self.name

    def get_ssl_display(self):
        return dict(self.SSL_CHOICES).get(self.ssl, self.ssl)



class Product_vps_hosting(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    vcpu = models.IntegerField()
    ram = models.IntegerField()
    ssd = models.IntegerField()
    os = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product_cloud_hosting(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    vcpu = models.IntegerField()
    ram = models.IntegerField()
    ssd = models.IntegerField()
    os = models.CharField(max_length=50)

    def __str__(self):
        return self.name
