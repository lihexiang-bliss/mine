# -*- coding: utf-8 -*-
import cekai.qiwei_tag.tag_api
import time


class TestTag():
    global current_time, tag_api, access_token
    current_time = str(int(time.time()))  # 时间戳取整
    tag_api = cekai.qiwei_tag.tag_api
    access_token = tag_api.get_access_token()

    def setup(self):
        # 添加标签前确认要添加的标签是否已存在,若已存在则删除
        tag_group = tag_api.get_corp_tag_list(access_token)
        for tag_group_ele in tag_group:
            if tag_group_ele['group_name'] == 'bliss' + current_time:
                for tag_ele in tag_group_ele['tag']:
                    if tag_ele['name'] == 'tag' + current_time:
                        tag_api.del_corp_tag(access_token, tag_ele['id'])

    def test_tag(self):
        # 创建一个标签并获取其id
        tag_group = tag_api.add_corp_tag(access_token, current_time)
        for tag in tag_group['tag']:
            if tag['name'] == 'tag' + current_time:
                tag_id = tag['id']

        # 删除刚新增的tag_id
        tag_api.del_corp_tag(access_token, tag_id)

        # 获取标签库 确认新增的标签已被删除
        r = tag_api.get_corp_tag_list(access_token)
        for tag_group_ele in r:
            if tag_group_ele['group_name'] == 'bliss' + current_time:
                for tag_ele in tag_group_ele['tag']:
                    assert tag_ele['name'] != 'tag' + current_time
