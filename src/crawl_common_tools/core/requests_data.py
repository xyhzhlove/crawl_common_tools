#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   requests_data.py
@Time    :   2024/09/05 13:06:41
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   如果请求到的数据是以控制台接口调用的形式去获取的，那么调用该方法
'''

from crawl_common_tools.utils.my_requests import MyRequests
from typing import Literal, Dict, Union, Any
from typing_extensions import Self


class RequestsData:

    # 类属性
    requests_instance = MyRequests.get_instance()

    # 调用时url参数后面的参数只可以以关键字的方式进行传参
    def __init__(self,
                 url: str,
                 *,
                 headers={'Content-Type': 'application/json'},
                 mod: Literal['GET', 'POST'],
                 params: Union[Dict, None] = None,
                 data: Union[Dict, None] = None) -> Self:

        # 实例属性访问该类属性
        self.requests_instance.headers.update(headers)
        self.url = url
        self.mod = mod
        self.params = params
        self.data = data

    def get_data(self) -> Any:
        result = None
        if self.mod == "GET":
            result = self.requests_instance.get(url=self.url,
                                                params=self.params)
        if self.mod == "POST":
            result = self.requests_instance.post(url=self.url, data=self.data)
        return result
