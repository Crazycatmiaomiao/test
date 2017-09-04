# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 15:31
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : baidu.py
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


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

print(driver.title)

driver.quit()