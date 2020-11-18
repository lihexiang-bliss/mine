# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
import allure
from cekai.app.xueqiu.base import Base
from cekai.app.xueqiu.market_page import MarketPage


class MainPage(Base):
    def goto_market(self):
        # 制造假的弹窗
        # self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.open_yaml('./main_page.yaml')
        return MarketPage(self.driver)
