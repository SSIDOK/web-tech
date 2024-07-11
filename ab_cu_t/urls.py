from django.urls import path
from . import views

app_name = 'ab_cu_t'

urlpatterns = [
    path('faq/', views.faq_page, name='faq_page'),
    path('PrivacyPolicy/', views.privacy_policy, name='privacy_policy'),
]