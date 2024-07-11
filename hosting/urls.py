from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hosting'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('form/', include('form.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('host/', include('host_page.urls')),
    path('ftp/', include('ftp_storage.urls')),
    path('', include('ab_cu_t.urls')),
    path('', include('domain_check.urls')),
    path('', include('contact.urls')),

]
