from django.contrib import admin
from .models import Product_virtual_hosting, Product_cloud_hosting, Product_vps_hosting

admin.site.register(Product_virtual_hosting)
admin.site.register(Product_vps_hosting)
admin.site.register(Product_cloud_hosting)
