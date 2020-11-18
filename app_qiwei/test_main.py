# -*- coding: utf-8 -*-
from cekai.app.qiwei.main_page import MainPage


class TestMain:
    def test_main(self):
        # 初始化通讯录中人员的数量为 0
        main = MainPage('0').goto_addresslist('0').goto_manage_addresslist().goto_editmember_page()
