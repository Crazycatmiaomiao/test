# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 10:25
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : webdriver的常用用法.py
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

urlone = 'http://www.baidu.com'
driver.get(urlone)
# 全屏化屏幕
driver.maximize_window()
shurukuangsize = driver.find_element_by_id('kw').size
print('输入框的尺寸%s'%shurukuangsize)
dibuwenjiantext = driver.find_element_by_id("cp").text
print(dibuwenjiantext)
# 获取属性值
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)
# 返回元素是否可见
fanhuiyuansushifoukejian = driver.find_element_by_id('kw').is_displayed()
print(fanhuiyuansushifoukejian)
driver.find_element_by_id('kw').send_keys('哎呀呀')
time.sleep(1)
driver.find_element_by_id('kw').clear()
time.sleep(1)
driver.find_element_by_id('kw').send_keys('哎呀呀wei')
time.sleep(1)

driver.find_element_by_id('su').click()
time.sleep(1)

driver.close()