# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 11:09
# @Author  : liqianyu
# @Email   : liqianyuwork@163.com
# @File    : 总体的获取浏览器进入百度.py
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

class come:
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    def come1(self):


        return self.driver,self.url
