#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   my_storage.py
@Time    :   2024/09/05 10:11:07
@Author  :   yonghui xu
@Version :   1.0
@Desc    :   存储的抽象类实现
'''
from abc import ABC, abstractmethod
from openpyxl import Workbook
from typing import Any, List, Union
from pathlib import Path
from crawl_common_tools.configs.storage_config import EXCEL_TITLE, EXCEL_PATH


class AbstractStorage(ABC):

    @abstractmethod
    def storage(self, data: Any) -> Union[Path, str]:
        pass


class ExcelStorage(AbstractStorage):

    def storage(self, data: List[List[str]]) -> Union[str, Path]:
        '''
        data的构成
        [
        ['表头1','表头2','表头3','表头4','表头5'],
        ['表头值1','表头值2','表头值3','表头值4','表头值5'],
        ['表头值1','表头值2','表头值3','表头值4','表头值5'],
        ['表头值1','表头值2','表头值3','表头值4','表头值5'],
        ]
        '''
        wb = Workbook()
        ws = wb.active
        ws.title = EXCEL_TITLE
        for d_item in data:
            ws.append(d_item)
        wb.save(EXCEL_PATH)
        return EXCEL_PATH
