# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from cekai.app.xueqiu.base import Base
from cekai.app.xueqiu.search_page import SearchPage


class MarketPage(Base):
    def goto_search(self):
        # self.find(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.open_yaml('./market_page.yaml')
        return SearchPage(self.driver)
