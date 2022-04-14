# 改变某一文件夹里所有文件的名字
import os
from pathlib import Path

class Change_Name():
    # 获取要传入names的个数
    def get_len(self, path):
        n = 0
        entries = os.listdir(path)
        for entry in entries:
            isdir = os.path.isdir(path + entry)
            if isdir:
                n += 1
        return n
    # 改变某一文件夹里所有文件的名字
    def change_isfile_name(self, path):
        n = 1
        entries = os.listdir(path)  # 返回一个Python列表,包括这个目录下所有的文件和文件夹
        for entry in entries:
            file_path = path + entry
            # isdir = os.path.isfile(file_path)  # 判断这个路径下的是文件吗 如果是返回True
            # if isdir:
            suffix = entry.split(".")[1]
            data_file = Path(file_path)
            data_file.rename(path + f'{str(n).zfill(5)}.{suffix}')  # 更改名字,后缀为文件本来的后缀名
            n += 1


    # 改变某一文件夹里所有文件的名字，传入后缀名
    def change_isfile_name_1(self, path, suffix): # Suffix:后缀名
        n = 1
        entries = os.listdir(path)  # 返回一个Python列表,包括这个目录下所有的文件和文件夹
        for entry in entries:
            file_path = path + entry
            isdir = os.path.isfile(file_path)  # 判断这个路径下的是文件吗 如果是返回True
            if isdir:
                data_file = Path(file_path)
                data_file.rename(path + f'{n}.{suffix}')  # 更改名字
                n += 1



if __name__ == '__main__':#作为脚本执行
    path = "C:/Users/10604/Desktop/yolov5/data/images/"#文件夹路径
    change_name = Change_Name()

    # len_names = change_name.get_len(path)  # 得到文件下文件夹的个数，确定传入名字的个数
    # names = ["hello", "the", "word"]
    change_name.change_isfile_name(path) # 修改文件下所有文件的名字,1....n,后缀名不变
    # change_name.change_isfile_name_1(path,"txt") # 修改文件下所有文件的名字，名字为：1.xx，2.xx，3.xx，4.xx....
    print("修改成功")






