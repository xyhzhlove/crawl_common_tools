#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   MySelenium.py
@Time    :   2024/09/05 09:16:43
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   关于浏览器驱动请求的封装
'''
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOption
from time import sleep
from typing import Union, List
from crawl_common_tools.configs.selenium_config.config import EDGE_DRIVER_PATH, WAIT_TIME
from crawl_common_tools.configs.logger_config import logger


class MySelenium:

    def __init__(self, url: str):
        self.url = url
        # 驱动得到的源码
        self.page_source = None

    def detail(self) -> Union[str, None]:
        # 创建Chrome选项对象
        options = EdgeOption()
        # 添加无头模式参数
        options.add_argument('--headless')
        # 可选：增加其他参数以提高稳定性
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('log-level=3')
        edge_service = EdgeService(executable_path=EDGE_DRIVER_PATH)
        driver = webdriver.Edge(service=edge_service, options=options)
        driver.get(self.url)
        sleep(WAIT_TIME)
        self.page_source = driver.page_source
        logger.info(f'{self.url}页面请求完成')
        return self.page_source
        # html_tree = etree.HTML(page_source)
