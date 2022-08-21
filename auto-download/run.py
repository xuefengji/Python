#!/use/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuefengji
@Create: 2021-01-19
@Update: 2021-01-29
@Description: 文件下载
"""

import requests
from .config import Config
import os
import time


class Run:
    def __init__(self):
        config = Config()
        self.download_path = config.download_path
        self.folder_name = config.folder_name
        self.folder_url = config.folder_url
        self.base_url = config.base_url
        self.headers = config.headers
        self.guid = config.folder_url.split('/')[2]
        self.root_path = os.path.join(config.download_path, config.folder_name)
        self.export_file = config.export_file
        self.total_files = 0
        self.download_success = 0
        self.download_fail = 0
        self.download_fail_files = []
        self.no_export = 0

    def get_all_files(self,headers,guid):
        """
        获取文件夹下的所有文件
        :param headers:
        :param guid:
        :return:
        """
        url = "https://shimo.im/lizard-api/files?collaboratorCount=true&folder={}".format(guid)
        try:
            data = requests.get(url=url, headers=headers, verify=False, stream=True)
            return data.json()
        except Exception as e:
            print("获取文件失败:{}".format(e))
            return ""

    def write_file(self,file_path,file_data):
        """
        将文件写入本地
        :param path: 写入的路径
        :param file_name: 写入的文件名
        :param export_type: 导出的类型
        :param file_data: 写入的数据
        :return:
        """
        try:
            with open(file_path, "wb") as f:
                for chunk in file_data.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print("下载完成！")
            self.total_files += 1
            self.download_success += 1
            return
        except Exception as e:
            self.total_files += 1
            self.download_fail += 1
            self.download_fail_files.append(file_path.split(self.download_path)[1][1:])
            if os.path.exists(file_path):
                os.remove(file_path)
            print("写入文件失败:{}".format(e))


    def download_file(self,path,file_name,file_type,file_guid,folder_guid):
        """
        根据不同的类型下载不同的文件
        :param path: 文件所在的文件夹路径
        :param file_name: 需要下载的文件名
        :param file_type: 文件存在石墨中的类型
        :param file_guid: 文件的 guid
        :param folder_guid: 文件所有文件夹的guid
        :return:
        """
        print(path)
        download_headers = self.headers.copy()
        download_headers["referer"] = self.base_url+"/"
        if not os.path.exists(path):
            os.makedirs(path)
        export_type = self.export_file[file_type]["select_export_type"]
        if export_type not in self.export_file[file_type]["export_types"]:
            print("无此类型下载")
            return
        file_path = os.path.join(path, file_name + '.' + export_type)
        if os.path.exists(file_path):
            print("此文件已存在，无需重复下载，文件：{}".format(file_path))
            return
        try:
            # 导出的 url 和参数
            url = "https://xxport.shimo.im/files/{}/export".format(file_guid)
            params_data = {
                "type": export_type,
                "file": "file_guid",
                "returnJson": 1,
                "name": "file_name"
            }
            # 类型为Excel表格的下载
            if file_type == "mosheet" or file_type == "sheet" :
                print(file_name)
                params_data['isAsync'] = 1
                # 为防止接口调用频繁限制速率
                time.sleep(60)
                res = requests.get(url=url, params=params_data, headers=download_headers, verify=False, stream=True)
                params_data = {
                    "taskId": res.json()['data']['taskId']
                }
                xlsx_url = "https://shimo.im/lizard-api/files/{}/export/progress".format(file_guid)
                xlsx_headers = self.headers.copy()
                xlsx_headers["referer"] = os.path.join(self.base_url,"folder/{}".format(folder_guid))
                while True:
                    res_data = requests.get(url=xlsx_url, params=params_data, headers=xlsx_headers, verify=False, stream=True)
                    if res_data.json()['data']['progress']==100:
                        break
                download_url = res_data.json()['data']['downloadUrl']
                download_headers["referer"] = self.base_url + "/"
                file_data = requests.get(url=download_url, headers=download_headers,  verify=False, stream=True)
                self.write_file(file_path, file_data)
                return
            # 其他类型的文件下载
            print(file_name)
            # 为防止接口调用频繁限制速率
            time.sleep(60)
            res = requests.get(url=url, params=params_data, headers=download_headers, verify=False, stream=True)
            print(res.json())
            file_data = requests.get(url=res.json()['redirectUrl'], headers=download_headers, verify=False, stream=True)
            self.write_file(file_path, file_data)
        except Exception as e:
            print("文件下载失败:{}".format(e))

    def search(self,headers,guid,file_path):
        """
        递归查找文件夹下是否有文件，有文件时,判断是文件时下载文件，没有时直接创建文件夹
        :param headers: 请求头
        :param guid: 文件夹的 guid
        :param file_path: 文件夹路径
        :return:
        """

        all_files = self.get_all_files(headers,guid)
        if len(all_files) == 0:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            return
        export_key= self.export_file.keys()
        for file in all_files:
            if not file['isFolder']:
                print(file['type'])
                if file['type'] not in export_key:
                    self.total_files += 1
                    self.no_export += 1
                    print("该类型无导出功能")
                    continue
                file_type = file['type']
                path = file_path
                file_name = file['name'].replace("/", "-")
                file_guid = file['guid']
                folder_guid = guid
                print("-----开始下载-----")
                self.download_file(path, file_name, file_type, file_guid, folder_guid)
                continue
            path = os.path.join(file_path,file['name'])
            header = self.headers.copy()
            header['referer'] = self.base_url+file['url']
            self.search(header,file['guid'],path)


if __name__ == "__main__":
    try:
        run = Run()
        run.search(run.headers,run.guid,run.root_path)
        print("本次需下载{}个文件，其中成功{}个，失败{}个，{}个无下载功能".format(run.total_files, run.download_success, run.download_fail, run.no_export))
        if len(run.download_fail_files):
            print("以下文件需要重新下载：")
            for fail_file in run.download_fail_files:
                print(fail_file)
    except Exception as e:
        print("程序异常：{}".format(e))