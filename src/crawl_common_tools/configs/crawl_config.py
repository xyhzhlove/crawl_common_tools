
CRAWL_RETURN_DATA_CONFIG = [
    {
        # url_address 是 目标网页的地址
        "url_address": "",
        # result_data 是该网页需要的数据，data_field是字段名  xpath为获取该字段的 xpath表达式
        "result_data": {
            "data_field1": "xpath1",
            "data_field2": "xpath2",
            "data_filed3": "xpath3",
        }
    },
    # 如果为多个字典，则表示多个目标网页，每个目标网页都以一个线程来执行
    {
        # url_address 是 目标网页的地址
        "url_address": "",
        # result_data 是该网页需要的数据，data_field是字段名  xpath为获取该字段的 xpath表达式
        "result_data": {
            "data_field1": "xpath1",
            "data_field2": "xpath2",
            "data_filed3": "xpath3"
        }
    }
]


