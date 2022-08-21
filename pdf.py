import fitz
import win32com.client
import os
import comtypes.client




def pdf_image(pdf_name):

    '''
    将pdf转换为图片
    :param pdf_name: pdf的路径
    :return:
    '''
    img_paths = []
    pdf = fitz.Document(pdf_name)
    for i,pg in enumerate(range(0, 2)):     #设置需要转换的页数
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(3.0, 3.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        # pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
        img_path = pdf_name[:-4] + '_' + str(pg+1) + '.jpg'
        pm.writePNG(img_path)  # 保存图片
        img_paths.append(img_path)
    pdf.close()
    return img_paths


# pdf_image("test.pdf")
if __name__ == '__main__':
    path = 'E:/work/11.ppt'
    pa = "E:/work"
    # fileNames = glob.glob(pa + r'\*')
    # for fileName in fileNames:     #将pa 文件夹中的文件删除。
    #     os.remove( fileName)
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application") #使用wps的接口
    powerpoint.Visible = 1
    ppt = powerpoint.Presentations.Open(path)
    print(ppt)
    # 另存为
    ppt.SaveAs('1.png', 17)
    # 退出
    ppt.Close()
    powerpoint.Quit()
