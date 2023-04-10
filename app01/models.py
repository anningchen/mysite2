from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

class Department(models.Model):
    title = models.CharField(max_length=16)

class Role(models.Model):
    caption = models.CharField(max_length=16)

"""
create table app01_userinfo(
id bigint auto_increment primary key,
name varchar(32),
password varchar(64),
age int
)
"""

##### 新增数据

# Deparment.objects.create(title="销售部")

