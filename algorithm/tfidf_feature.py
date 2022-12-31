"""
文章分词
提供两种方案：
"""

import jieba
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import Bunch
from concurrent import futures
import sys
import pickle

userdict = './词典.txt'
jieba.load_userdict(userdict)


def tokenizer():
    return jieba


def readfile(filepath, encoding='gb18030'):
    # 读取文本
    with open(filepath, "rt", encoding='utf-8',errors='ignore') as fp:
        content = fp.read()
    return content


def savefile(savepath, content):
    # 保存文本
    with open(savepath, "wt",encoding='utf-8',errors='ignore') as fp:
        fp.write(content)


def writeobj(path, obj):
    # 持久化python对象
    with open(path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def readobj(path):
    # 载入python对象
    with open(path, "rb",encoding='utf-8',errors='ignore') as file_obj:
        obj = pickle.load(file_obj)
    return obj


def check_dir_exist(dir):
    # 坚持目录是否存在，不存在则创建
    if not os.path.exists(dir):
        os.mkdir(dir)


def folder_handler(args):
    """遍历一个文件夹下的文本"""
    folder, encoding, seg = args
    print('遍历：', folder)
    try:
        assert os.path.isdir(folder)
    except AssertionError:
        return None
    files = os.listdir(folder)
    content = []
    filenames = []
    for name in files:
        if name.startswith('.DS'):
            continue
        filepath = os.path.join(folder, name)
        text = readfile(filepath, encoding)
        # 在此可直接分词
        if seg:
            text = ' '.join(jieba.cut(text))
        content.append(text)
        filenames.append(filepath)

    return (filenames, content)


def corpus_bunch(data_dir, encoding='utf-8', seg=True, tier=2):
    """
    得到文本库，返回一个 Bunch 对象
    :param data_dir:    文本库目录，目录下以文件归类 data_dir/category/1.txt
    :param encoding:    文本库编码
    :param seg:         是否需要分词
    :param tier:        data_dir 目录下的层级 2: data_dir/category/1.txt, 1: data_dir/1.txt
    :return:
    """
    try:
        assert os.path.isdir(data_dir)
    except AssertionError:
        print('{} is not a folder!')
        sys.exit(0)
    try:
        assert tier in [1, 2]
    except AssertionError:
        print('目录层级 tier 只能是 1 或 2！')
        sys.exit(0)
    corpus = Bunch(filenames=[], label=[], contents=[])
    if tier == 2:
        folders = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if not d.startswith('.DS')]

    else:
        folders = [data_dir]
    # 创建线程池遍历二级目录
    with futures.ThreadPoolExecutor(max_workers=len(folders)) as executor:
        folders_executor = {executor.submit(folder_handler, (folder, encoding, seg)): folder for folder in folders}
        for fol_exe in futures.as_completed(folders_executor):
            folder = folders_executor[fol_exe]
            filenames, content = fol_exe.result()
            if content:

                cat_name = folder.split('/')[-1]
                cat_name = cat_name.split("\\")[-1]

                content_num = len(content)
                print(cat_name, content_num, sep=': ')
                label = [cat_name] * content_num
                corpus.filenames.extend(filenames)
                corpus.label.extend(label)
                corpus.contents.extend(content)
    return corpus


def vector_space(corpus_dir, stop_words=None, vocabulary=None, encoding='utf-8', seg=True, tier=2):
    """将一个语料库向量化"""
    vectorizer = TfidfVectorizer(stop_words=stop_words, vocabulary=vocabulary)

    corpus = corpus_bunch(corpus_dir, encoding='utf-8', seg=seg, tier=tier)
    tfidf_bunch = Bunch(filenames=corpus.filenames, label=corpus.label, tdm=[], vocabulary={})

    tfidf_bunch.tdm = vectorizer.fit_transform(corpus.contents)
    tfidf_bunch.vocabulary = vectorizer.vocabulary_
    return tfidf_bunch


def tfidf_space(data_dir, save_path, stopword_path=None, encoding='utf-8',seg=True):

    stpwd = None
    if stopword_path:
        stpwd = [wd.strip() for wd in readfile(stopword_path).splitlines()]
    check_dir_exist(save_path)
    train = data_dir + 'train_seg'
    train_tfidf = vector_space(train, stop_words=stpwd, encoding='utf-8', seg=seg)

    test = data_dir + 'test_seg'
    test_tfidf = vector_space(test, stop_words=stpwd, vocabulary=train_tfidf.vocabulary, seg=seg)

    writeobj(os.path.join(save_path, 'train_tfidf.data'), train_tfidf)
    writeobj(os.path.join(save_path, 'test_tfidf.data'), test_tfidf)
    writeobj(os.path.join(save_path, 'vocabulary.data'), train_tfidf.vocabulary)


if __name__ == '__main__':
    data_dir = './CS/'

    # 构建词袋
    tfidf_space(data_dir, data_dir + 'fearture_space', stopword_path=data_dir + 'stopword.txt',seg=True)
