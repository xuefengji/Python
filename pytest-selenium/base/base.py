"""
基类：封装基础操作
"""


class Base:
    # 获取 driver
    def get_driver(self):
        pass
    # 定位元素
    def get_element(self):
        pass
    # 输入值
    def send_key(self):
        pass

    # driver 退出
    def quit(self):
        pass
