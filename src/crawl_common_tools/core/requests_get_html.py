#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   requests_get_html.py
@Time    :   2024/09/05 10:46:50
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   如果请求到的内容直接是一个完整的网页内容，即需要的内容是直接可以请求到的，那么调用该方法进行内容爬取
'''
from typing import Union
from crawl_common_tools.utils.my_requests import MyRequests
from crawl_common_tools.configs.requests_config import RESPONSE_ENCODING
from crawl_common_tools.configs.logger_config import logger


class GetHtml:
    # 类属性
    request_instance = MyRequests.get_instance()

    @classmethod
    def crawl(cls, url: str) -> Union[str, None]:
        html_str = None
        response = cls.request_instance.get(url=url)
        if response.status_code == 200:
            logger.info(f'{url}请求完成')
            response.encoding = RESPONSE_ENCODING
            html_str = response.text
            return html_str
        else:
            logger.error(f'{url}请求失败')
            return html_str
