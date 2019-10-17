"""
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""

# import os
#
#
# def search_file(path, str):
#     for file in os.listdir(path):
#         this_path = os.path.join(path, file)
#         if os.path.isfile(this_path):
#             if str in file:
#                 print(this_path)
#         else:
#             search_file(this_path, str)
# search_file(os.path.abspath(".."), "py")

import os  # 引入os


def search_file(path, str):  # 传入当前的绝对路径以及指定字符串
    # 首先先找到当前目录下的所有文件
    for file in os.listdir(path):  # os.listdir(path) 是当前这个path路径下的所有文件的列表
        this_path = os.path.join(path, file)
        if os.path.isfile(this_path):  # 判断这个路径对应的是目录还是文件，是文件就走下去
            if str in file:
                yield this_path
            else:
                continue
        else:   # 不是就再次执行这个函数，递归下去

            search_file(this_path, str)  # 递归下去


for i in search_file(os.path.abspath(".."), "py"):
    print(i)

