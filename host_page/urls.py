from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'host_page'

urlpatterns = [
    path('virtual_hosting/', views.virtual_host, name='host'),
    path('vps-hosting/', views.vps_hosting_view, name='vps_hosting_view'),
    path('cloud-hosting/', views.cloud_hosting_view, name='cloud_hosting_view'),

]