# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from cekai.app.qiwei.base import Base
from cekai.app.qiwei.manage_addresslist_page import ManageAddresslistPage


class AddresslistPage(Base):
    def goto_manage_addresslist(self):
        ele = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"共")]')
        self.num = ele.text[1]
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gup']").click()

        return ManageAddresslistPage(self.num, self.driver)
