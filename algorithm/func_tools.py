"""
工具函数
"""
import os
import pickle


def readfile(filepath, encoding='utf-8'):
    # 读取文本
    with open(filepath, "rt", encoding=encoding) as fp:
        content = fp.read()
    return content


def savefile(savepath, content):
    # 保存文本
    with open(savepath, "wt") as fp:
        fp.write(content)


def writeobj(path, obj):
    # 持久化python对象
    with open(path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def readobj(path):
    # 载入python对象
    with open(path, "rb") as file_obj:
        obj = pickle.load(file_obj)
    return obj


def check_dir_exist(dir):
    # 坚持目录是否存在，不存在则创建
    if not os.path.exists(dir):
        os.mkdir(dir)
