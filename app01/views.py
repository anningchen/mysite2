from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import UserInfo, Department


# Create your views here.


def info_list(request):
    # 获取数据库中所有的用户信息

    data_list = UserInfo.objects.all()

    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')

    elif request.method == 'POST':
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        age = request.POST.get("age")
        UserInfo.objects.create(name=username,password=pwd,age=age)
        return redirect("/info/list/")

def info_delete(request):

    id = request.GET.get('id')
    UserInfo.objects.filter(id=id).delete()
    return redirect("/info/list/")

def orm(reqeust):
    data = UserInfo.objects.all()
    Department.objects.create(title="销售部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="交易部")

    print(data)
    return HttpResponse("hello")
