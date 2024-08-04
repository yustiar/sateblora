"""
URL configuration for sateblora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('load_more_infografis', views.load_more_infografis, name='load_more_infografis'),

    path('load_init_pub', views.load_init_pub, name='load_init_pub'),
    path('load_more_pub', views.load_more_pub, name='load_more_pub'),
    path('detail_pub', views.detail_pub, name='detail_pub'),
    path('cari_pub', views.cari_pub, name='cari_pub'),

    path('load_init_brs', views.load_init_brs, name='load_init_brs'),
    path('load_more_brs', views.load_more_brs, name='load_more_brs'),
    path('detail_brs', views.detail_brs, name='detail_brs'),
    path('cari_brs', views.cari_brs, name='cari_brs'),
]
