from django.shortcuts import render
from django.http import JsonResponse
from .models import Product_virtual_hosting, Product_cloud_hosting, Product_vps_hosting


def virtual_host(request):
    products_virtual = Product_virtual_hosting.objects.all()
    return render(request, 'host_page/virtual_host.html', {'products_virtual': products_virtual})
    #return render(request, 'host_page/virtual_host.html')


def vps_hosting_view(request):
    products_vps = Product_vps_hosting.objects.all()
    return render(request, 'host_page/vps_hosting.html', {'products_vps': products_vps})
    #return render(request, 'host_page/vps_hosting.html')


def cloud_hosting_view(request):
     products_cloud = Product_cloud_hosting.objects.all()
     return render(request, 'host_page/cloud_hosting.html', {'products_cloud': products_cloud})
   # return render(request, 'host_page/cloud_hosting.html')
