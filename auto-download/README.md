# shimo-auto-download

## 项目说明

本项目为解决自动下载文档到本地存档



## 运行环境

+ Python 3.8
+ requests 库版本 2.25.1
+ 可使用 pip install -r requirements.txt 进行安装 requests



## 项目介绍

+ 项目结构

  ```
  shimo-auto-download
  │  .gitignore
  │  config.py            
  │  README.md
  │  requirements.txt    
  │  run.py               
  ```

  config.py : 项目的配置文件，运行前必须先配置相应的必填项

  相关必填项：

  download_path: 下载的本地路径

  folder_name：需要下载的入口文件夹的名字

  folder_url：入口文件夹的 url

  headers->cookie：登录后的 cookie 信息

  export_file->select_export_type：文件的导出类型

  

  run.py：进行文件下载的文件

  相关函数：

  get_all_files：获取文件夹下所有文件

  write_file：将文件写入本地

  download_file：文件下载

  search：文件查找

  

  requirements.txt ：安装的库的版本文件

  

  ## 项目运行

  执行命令：python  run.py

  