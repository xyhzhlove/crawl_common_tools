#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   my_thread_pool.py
@Time    :   2024/09/05 09:47:46
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   线程池的封装
'''
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any, List
from crawl_common_tools.configs.thread_pool_config import MAX_WORKERS


class MyThreadPool:

    def __init__(self, cb: Callable[[str], Any], urls: List[str]):
        '''
        传递进来的cb是一个函数,函数只接收一个参数那就是字符串类型的url,返回值为任意类型即Any
        urls为一个字符串形式的列表,这里为url列表
        '''
        self.cb = cb
        self.urls = urls

    def run(self):
        result: List[Any] = []
        # 创建一个最大容纳4个线程的线程池
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # 准备要处理的数据
            # 提交任务到线程池
            results = [executor.submit(self.cb, url) for url in self.urls]

            # 收集结果
            for future in results:
                result.append(future.result())
        # 跳出with语句后表示线程池操作执行完毕，从而可以执行以下操作
        return result
