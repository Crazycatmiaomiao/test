# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 11:04
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : 键盘事件.py
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
# keys  方法中包含了键盘操作方法
from selenium.webdriver.common.keys import Keys
import login
import time

b = login.come()
driver = b.driver
url = b.url
driver.get(url)

# 输入框输入内容
driver.find_element_by_id('kw').send_keys('seleniumm')
time.sleep(1)
# 删除一个字符
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(1)
# 空格加教程
driver.find_element_by_id('kw').send_keys(Keys.SPACE,"教程")
time.sleep(1)

# 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(1)

# 剪切输入框内容 字母必须用小写，大写不识别
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(1)

# 粘贴输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
time.sleep(1)

# 利用回车键代替单击

driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.F12)
time.sleep(2)


driver.close()
