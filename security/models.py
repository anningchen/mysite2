from django.db import models


# Create your models here.

class Security(models.Model):
    code = models.CharField(max_length=6, verbose_name='代码', primary_key=True)
    name = models.CharField(max_length=8, verbose_name='名称')
    industry = models.CharField(max_length=32, verbose_name='所属行业')
    create_date = models.DateTimeField(auto_now_add=True)
