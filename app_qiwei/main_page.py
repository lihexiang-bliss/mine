# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from cekai.app.qiwei.addresslist_page import AddresslistPage
from cekai.app.qiwei.base import Base


class MainPage(Base):
    def goto_addresslist(self, num):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        return AddresslistPage(num, self.driver)
