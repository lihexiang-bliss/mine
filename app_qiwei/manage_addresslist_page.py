# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from cekai.app.qiwei.base import Base
import time


class ManageAddresslistPage(Base):
    def goto_editmember_page(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/b00"]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        time.sleep(10)
        ele = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"共")]')
        after_num = ele.text[1]
        assert int(self.num) == int(after_num) + 1
