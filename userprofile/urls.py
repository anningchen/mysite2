from django.urls import path, include
from . import  views

app_mame = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
