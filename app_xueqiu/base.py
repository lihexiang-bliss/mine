# -*- coding: utf-8 -*-
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from cekai.app.xueqiu.handle_blank import handle_blank

with open('./base.yaml') as f:
    content = yaml.safe_load(f)
    caps = content['caps']
    ip = content['server']['ip']
    port = content['server']['port']


class Base:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    def open_yaml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
        self.parse_yaml(data['steps'])

    def parse_yaml(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send_keys' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step['content'])

    @handle_blank
    def find(self, by, locator):
        if locator == None:
            # 如果只传一个参数
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result
