import os
def delete_file(path):
    filelist = os.listdir(path)
    for file in filelist:
        oldpath = os.path.join(path, file)
        filename = os.path.splitext(file)[0]  # 文件名
        filetype = os.path.splitext(file)[1]  # 文件类型
        if filename[1] < '4':
            os.remove(oldpath)

if __name__ == '__main__':#作为脚本执行
    path = "C:/Users/10604/Desktop/yolov5/BDD_DATA/labels/train/"#文件夹路径
    delete_file(path)
    print("修改成功")
