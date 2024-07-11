from django.urls import path
from . import views

app_name = 'domain_check'

urlpatterns = [
    path('domain_check/', views.domain_check_page, name='domain_check_page'),
]