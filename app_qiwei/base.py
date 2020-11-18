# -*- coding: utf-8 -*-
import yaml
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

with open('./base.yaml') as f:
    content = yaml.safe_load(f)
    caps = content['caps']
    ip = content['server']['ip']
    port = content['server']['port']


class Base:
    def __init__(self, num, driver: WebDriver = None):
        # num 为通讯录中人员的数量
        if driver == None:
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver = driver
        self.num = num
