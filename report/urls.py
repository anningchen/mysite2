from django.urls import path, include
from . import  views

app_mame = 'report'

urlpatterns = [
    path('report-list/', views.report_list, name='report_list'),

]
