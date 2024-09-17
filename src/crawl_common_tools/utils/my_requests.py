#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   my_requests.py
@Time    :   2024/09/05 09:39:11
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   requests库的公共封装
'''
import requests
from crawl_common_tools.configs.requests_config import REQUESTS_HEADER, REQUESTS_PROXIES


class MyRequests:

    @staticmethod
    def get_instance():
        # 创建一个会话
        instance = requests.Session()
        instance.headers.update(REQUESTS_HEADER)
        instance.proxies.update(REQUESTS_PROXIES)
        return instance
