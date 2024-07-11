from django.shortcuts import render


def faq_page(request):
    return render(request, 'ab_cu_t/faq.html')


def privacy_policy(request):
    return render(request, 'ab_cu_t/PrivacyPolicy.html')
