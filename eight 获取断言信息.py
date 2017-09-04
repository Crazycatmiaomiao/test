# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 11:53
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : eight 获取断言信息.py
# @Software: PyCharm Community Edition
"""
-------------------------------------------------------------------------------

code is far away from bugs with the god animal protecting
               ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
-------------------------------------------------------------------------------
"""

import login,time
driver = login.come().driver
url = login.come().url
driver.get(url)
print('before search.===================')

# 打印当前页面title
pagetitle = driver.title
print(pagetitle)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(1)

print('after search.===================')
# 再次打印title
title = driver.title
print(title)
time.sleep(1)

#现在的网址
nowurl = driver.current_url
print(nowurl)
time.sleep(1)

# 获取结果数目
user = driver.find_element_by_class_name('nums').text
print(user)

time.sleep(1)

