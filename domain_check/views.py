from django.shortcuts import render
from .models import Domain


def domain_check_page(request):
    domains = Domain.objects.all()
    return render(request, 'domain_check/domain_check.html', {'domains': domains})
