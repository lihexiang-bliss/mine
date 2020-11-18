# -*- coding: utf-8 -*-
from cekai.app.xueqiu.main_page import MainPage


class TestMain:
    def test_main(self):
        main = MainPage().goto_market().goto_search().search()
