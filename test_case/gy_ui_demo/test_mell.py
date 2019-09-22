#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/20'
# def test_loglin(driver):
#    # 打开商城网页
#    driver.get("打开登录界面","http://qa.yansl.com/#/login")
#    # driver.send_keys("输入用户名",'//input[@name="username"]')# 运行不了
#    # driver.send_keys("输入密码",'//input[@name="password"]') 运行不了
#    # driver.click("点击登录",'//span[contains(text(),"登录")]') 运行不了


def test_uiysl(driver):
   # 打开http://ui.yansl.com/#/randomCode网页
   # 打开单选框,输入框
   driver.get("打开Ui界面","http://ui.yansl.com/#/input")
   driver.click("点击表单元素",'(//div[@class="el-submenu__title"])[1]')
   driver.send_keys("输入内容",'//input[@name="t1"]',"nihao")
   driver.click("点击单选框","//li[text()='单选框(3)']")
   driver.click("选择女","//input[@value='1']")
   driver.click("选择备选项1","(//span[@class='el-radio__inner'])[1]")
   # 打开多选框
   driver.get("打开多选页面","http://ui.yansl.com/#/checkbox")
   driver.click("点击表单元素", '(//div[@class="el-submenu__title"])[1]')
   driver.click("点击多选框","//li[text()='多选框(4)']")
   driver.click("点击纯多选框重庆", '//input[@value="2"]')
   driver.click("点击纯多选框河南", '//input[@value="3"]')
   driver.click("点击多选框2 linux","//span[text()='linux']")
   driver.click("点击多选框2 mysql", "//span[text()='mysql']")
   driver.click("点击多选框3全选","//span[text()='全选']")
   driver.click("多选框4","(//span[text()='上海'])[2]")
   # 打开下拉框
def test_uiys2(driver):
   driver.get("打开下拉框界面","http://ui.yansl.com/#/select")
   driver.click("点击表单元素", '(//div[@class="el-submenu__title"])[1]')
   driver.click("点击下拉框","//li[text()='下拉框(6)']")
   driver.click("点击纯下拉框","//select[@name='item1']")
   driver.select_by_index("点击纯下拉框","//select[@name='item1']",3) # 用下标定位
   driver.select_by_index("点击纯下拉框", "//select[@name='item1']", 0)
   driver.select_by_index("点击纯下拉框", "//select[@name='item1']", 2)