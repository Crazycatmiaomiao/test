# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 15:21
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : ten定位一组元素.py
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
from selenium import webdriver

import login,time
driver = login.come.driver
url = login.come.url
driver.get(url)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(1)

textlist = driver.find_elements_by_xpath('//div/h3/a')

for i in textlist:
    print(i.text)