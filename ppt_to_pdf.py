import comtypes.client
import os
import win32
import glob

if __name__ == '__main__':
    path = 'E:/myself/project/Python/11.ppt'
    pa = "E:/myself/project/Python/1/"
    fileNames = glob.glob(pa + r'\*')
    for fileName in fileNames:  # 将pa 文件夹中的文件删除。
        os.remove(fileName)
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")  # 使用wps的接口
    # powerpoint.Visible = 1
    ppt = powerpoint.Presentations.Open(path)
    # 另存为
    ppt.SaveAs(pa + '.jpg', 17)
    # 退出
    ppt.Close()

