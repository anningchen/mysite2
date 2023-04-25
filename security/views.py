from datetime import date, timedelta

import tushare as ts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

ts.set_token('fa344a3cdf4598402ab437dc37b519d47bd2296b598e429c70ba0a01')
pro = ts.pro_api()


def from_code_to_ts_code(code):
    first_letter = code[0]
    if first_letter == '6':
        code += '.SH'
    elif first_letter == '0' or '3':
        code += '.SZ'
    return code


label = ['股票代码', '股票名称', '最新价', '最高价', '涨跌幅', '最低价', '开盘价', '昨收',
         '涨停', '跌停', '成交量(手)', '成交额', '外盘', '量比', '均价',
         '总市值', '流通市值', '市盈(动)', '静市盈率', '滚动市盈率', '市净率',
         '换手率', 'ROE']


# Create your views here.
@login_required(login_url='/userprofile/login/')
def security_list(request, ):
    code_list = ['000813', '000899', '000722', '002709', '000733', '603963',
                 '603329', '300593', '605117', '603429', '002557', '002426', '000006',
                 '002216']
    today = date.today().strftime("%Y%m%d")
    start_date = date.today() - timedelta(10)  # 十天前
    security_list = []
    for code in code_list:
        ts_code = from_code_to_ts_code(code)
        name, industry = pro.stock_basic(ts_code=ts_code).loc[0, ['name', 'industry']]
        security_list.append({"code": code, "name": name, "industry": industry})

    context = {'today': str(date.today()), "security_list": security_list}

    return render(request, 'security/list.html', context)
