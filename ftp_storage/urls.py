from django.urls import path
from . import views

app_name = 'ftp_storage'

urlpatterns = [
    path('', views.ftp_page, name='ftp_page'),

]
