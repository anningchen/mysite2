from django.urls import path

from . import views

app_mame = 'security'

urlpatterns = [
    path('list/', views.security_list, name='security_list'),

]
