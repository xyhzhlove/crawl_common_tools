#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   selenium_get_html.py
@Time    :   2024/09/05 13:06:41
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   如果请求到的内容直接是一个不完整的网页内容，即需要的内容是需要等到页面加载才可以得到的，那么调用该方法进行内容爬取
'''
from typing import Union
import traceback
from crawl_common_tools.utils.my_selenium import MySelenium
from crawl_common_tools.configs.logger_config import logger


class GetHtml:

    def __init__(self, url: str):
        self.url = url

    def crawl(self) -> Union[str, None]:
        html_str = None
        try:
            my_selenium_instance = MySelenium(url=self.url)
            html_str = my_selenium_instance.detail()
            return html_str
        except Exception as e:
            logger.error(traceback.format_exc())
            return html_str
