# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 10:15
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : 控制浏览器操作.py
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
import time

driver = webdriver.Chrome()
driver.set_window_size(480,880)

firsturl ='http://www.baidu.com'
print('百度的网站%s'%(firsturl))
driver.get(firsturl)
time.sleep(1)

seconedurl = 'http://news.baidu.com'
print('百度图库%s'%seconedurl)
driver.get(seconedurl)
time.sleep(1)

print('后退到百度首页')

driver.back()
time.sleep(1)

print('前进到新闻页')
driver.forward()
time.sleep(1)
driver.close()

