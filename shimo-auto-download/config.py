#!/use/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuefengji
@Create: 2021-01-19
@Update: 2021-01-21
@Description: 配置项
"""


class Config():
    base_url = "https://shimo.im"
    # 必填项：下载的本地路径
    download_path= "G:\download"
    # 必填项：当前入口文件夹的名字
    folder_name = "测试部"
    # 必填项：当前入口文件夹的url
    folder_url = "/folder/zr6jmBLglnIZaMZK"
    # 请求头部信息，其中 cookie 必填
    headers = {
        "cookie": "shimo_gatedlaunch=1; shimo_kong=0; shimo_svc_edit=7570; sdk_v2_comment=3717; _bl_uid=5vkzbjFRxsayOI2Rg1vqwybdRw7b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2234648131%22%2C%22%24device_id%22%3A%2217704e32990829-09a4476736e21-c791039-2073600-17704e32991aa0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2217704e32990829-09a4476736e21-c791039-2073600-17704e32991aa0%22%7D; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1609118657,1609840190,1610370890,1611020718; shimo_sid=s%3AKSIfL4NBwVw80K68vKqCEINw73vSooPs.UFO3F4lJYmuJgRoXpE10F7XdnD9BzuyKrcwNfFQ98pw; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2234648131%22%2C%22%24device_id%22%3A%2217704e32990829-09a4476736e21-c791039-2073600-17704e32991aa0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2217704e32990829-09a4476736e21-c791039-2073600-17704e32991aa0%22%7D; _csrf=VA0HI3-N_G8-m2mM89IfylMP; deviceId=c0d7b354-d45e-4ad8-8b6e-4b9a2d4f0e28; deviceIdGenerateTime=1611537967203; sensorsdata2015session=%7B%7D; sensorsdata2015session=%7B%7D; acw_tc=2760824e16115401340115020ea6b37207192411f8ce64373f2b4b8263f322",
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

