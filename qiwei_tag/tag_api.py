# -*- coding: utf-8 -*-
import requests


# 获取access_token
def get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    params = {'corpid': 'ww96a090184a87f67b', 'corpsecret': 'vWybVP4ixcnodYHEcZyShZxuJARte-ZL5EPjfYkrre8'}
    r = requests.get(url, params=params)
    access_token = r.json()['access_token']
    return access_token


# 获取企业标签库
def get_corp_tag_list(access_token):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
    params = {'access_token': access_token}
    r = requests.post(url, params=params)
    tag_group = r.json()['tag_group']
    return tag_group


# 添加企业客户标签
def add_corp_tag(access_token, current_time):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
    params = {'access_token': access_token}
    json = {'group_name': 'bliss' + current_time, 'tag': [{'name': 'tag' + current_time}]}
    r = requests.post(url, params=params, json=json)
    tag_group = r.json()['tag_group']
    return tag_group


# 删除企业客户标签
def del_corp_tag(access_token, tag_id):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
    params = {'access_token': access_token}
    json = {'tag_id': [tag_id]}
    r = requests.post(url, params=params, json=json)
    print(r.json())
