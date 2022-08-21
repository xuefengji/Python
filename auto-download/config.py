#!/use/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuefengji
@Create: 2021-01-19
@Update: 2021-01-21
@Description: 配置项
"""


class Config():
    base_url = "下载的网址"
    # 必填项：下载的本地路径
    download_path= "文件路径"
    # 必填项：当前入口文件夹的名字
    folder_name = "文件名"
    # 必填项：当前入口文件夹的url
    folder_url = "下载的路径"
    # 请求头部信息，其中 cookie 必填
    headers = {
        "cookie": "cookies",
        "referer": base_url+folder_url
    }
    # 类型配置，其中 select_export_type 必填，为需要导出的文件格式
    export_file={
        "newdoc":{
            "export_types":["pdf","docx","jpg","md"],
            "select_export_type":"docx"
        },
        "mosheet": {
            "export_types": ["xlsx"],
            "select_export_type": "xlsx"
        },
        "modoc": {
            "export_types": ["pdf","docx","wps"],
            "select_export_type": "docx"
        },
        "presentation": {
            "export_types": ["pdf","pptx"],
            "select_export_type": "pptx"
        },
        "mindmap": {
            "export_types": ["xmind","jpg"],
            "select_export_type": "xmind"
        },
        "sheet":{
            "export_types": ["xlsx"],
            "select_export_type": "xlsx"
        }
    }

