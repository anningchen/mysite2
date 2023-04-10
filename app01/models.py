from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    # 无约束
    # department_id = models.BigIntegerField(verbose_name='部门ID')
    # 有约束

    #  - to, 与那张表关联
    #  - to_field, 与表中的那一列关联

    # - 级联删除,CASCADE
    depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)

    gender_choices = (
        (1, '男'),
        (2, '女'),

    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    create_time = models.DateTimeField(verbose_name='入职时间')


class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='部门名称')


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
