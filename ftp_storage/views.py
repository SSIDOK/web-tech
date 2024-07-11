from django.shortcuts import render
from .models import Product_ftp_storage


def ftp_page(request):
    # return render(request, 'ftp_storage/ftp_storage.html')
    products_ftp = Product_ftp_storage.objects.all()
    return render(request, 'ftp_storage/ftp_storage.html', {'products_ftp':products_ftp})
