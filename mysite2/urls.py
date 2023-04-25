"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from app01 import views
from app01.views import info_list, info_add, info_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户管理
    path('info/list/', info_list),
    path('info/add/', info_add),
    path('info/delete/', info_delete),
    path('depart/list/', views.depart_list),
    path('index/', views.index),
    path('userprofile/', include(('userprofile.urls', 'userprofile'), namespace='userprofile')),
    path('report/', include(('report.urls', 'report'), namespace='report')),
    path('security/', include(('security.urls', 'security'), namespace='security'))

]
