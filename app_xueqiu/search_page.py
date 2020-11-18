# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from cekai.app.xueqiu.base import Base


class SearchPage(Base):
    def search(self):
        # self.find(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('alibaba')
        self.open_yaml('./search_page.yaml')
