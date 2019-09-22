# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/31 14:31
import pytest
import os
from selenium import webdriver

from config.config import PRJ_ROOT_PATH
from tools.ui.base_ui import BaseUI

@pytest.fixture(scope='session')
def driver():
    driver_path = os.path.join(PRJ_ROOT_PATH, "chrome_driver/chromedriver.exe")
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(8)  # 设置隐式时间等待
    base = BaseUI(driver)
    yield base
    driver.quit()