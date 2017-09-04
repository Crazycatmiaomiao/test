# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 14:21
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : nine 设置元素等待.py
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
# 显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import login
driver = login.come.driver
url = login.come.url
# driver.get(url)
#
# element = WebDriverWait(driver, 2, 0.5).until(
#                       EC.presence_of_element_located((By.ID, "kw"))
#                       )
# element.send_keys('selenium')
# #  隐式等待
# driver.quit()

from time import ctime

from selenium.common.exceptions import NoSuchElementException
driver.implicitly_wait(10)
driver.get(url)
try:
    print(ctime())
    driver.find_element_by_id('kw22').send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()