#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   logger_config.py
@Time    :   2024/09/05 08:53:29
@Author  :   yonghui xu 
@Version :   1.0
@Desc    :   日志配置
'''

import logging
from logging import handlers


def setup_logger(*, log_file='app.log', log_level=logging.DEBUG):
    # 只可以以关键字的方式传参
    '''
    DEBUG: 这是最详细的日志信息，主要用于开发阶段调试代码使用。
    INFO: 通常用于记录程序运行的基本情况，如进程启动、结束等。
    WARNING: 表示一种潜在的问题，它不会阻止程序的正常运行，但需要引起注意。
    ERROR: 记录错误信息，表明发生了某个问题，导致某些功能无法正常执行。
    CRITICAL: 最严重的错误级别，表示发生致命错误，可能导致整个程序或系统不可用。
    当你创建一个Logger对象并设置其日志级别时，只有等于或高于所设级别的日志记录才会被处理。例如，如果你设置日志级别为WARNING，那么WARNING, ERROR, 和CRITICAL级别的日志信息会被记录下来，而DEBUG和INFO级别的日志则不会。
    '''
    # 创建logger对象
    logger = logging.getLogger('my_logger')
    logger.setLevel(log_level)

    # 创建handler，用于写入日志文件
    file_handler = handlers.RotatingFileHandler(log_file,
                                                maxBytes=1024 * 1024,
                                                backupCount=5,
                                                encoding='utf8')
    file_handler.setLevel(log_level)

    # 再创建一个handler，用于输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # 定义日志输出格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
