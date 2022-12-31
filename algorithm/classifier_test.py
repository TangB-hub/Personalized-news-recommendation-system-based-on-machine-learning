"""
文本分类
实现读取文本，实现分词，构建词袋，保存分词后的词袋。
提取 tfidf 特征，保存提取的特征
"""
import os
from sklearn.externals import joblib
from sklearn import metrics
import func_tools as ft
from tfidf_feature import vector_space
from sklearn.feature_extraction.text import TfidfVectorizer


class TextClassifier:

    def __init__(self, clf_model, data_dir, model_path):
        """
        分类器
        :param clf_model:   分类器算法模型
        :param data_dir:    特征数据存放位置
        :param model_path:  模型保存路径
        """
        self.data_dir = data_dir
        self.model_path = model_path
        self.train_data = os.path.join(data_dir, 'train_tfidf.data')
        self.test_data = os.path.join(data_dir, 'test_tfidf.data')
        self.vocabulary_data = os.path.join(data_dir, 'vocabulary.data')
        self.clf = self._load_clf_model(clf_model)

    def _load_clf_model(self, clf_model):
        if os.path.exists(self.model_path):
            print('loading exists model...')
            return joblib.load(self.model_path)
        else:
            print('training model...')
            train_set = ft.readobj(self.train_data)
            clf = clf_model.fit(train_set.tdm, train_set.label)

#            joblib.dump(clf, self.model_path)
            return clf

    def _predict(self, tdm):
        """
        :param tdm:     # 特征矩阵
        :return:
        """

        return self.clf.predict(tdm)



    def validation(self):
        """使用测试集进行模型验证"""
        print('starting validation...')
        test_set = ft.readobj(self.test_data)
        predicted = self._predict(test_set.tdm)

        actual = test_set.label
        for flabel, file_name, expct_cate in zip(actual, test_set.filenames, predicted):
            if flabel != expct_cate:
                print(file_name, ": 实际类别:", flabel, " --> 预测类别:", expct_cate)
        print('准确率: {0:.10f}'.format(metrics.precision_score(actual, predicted, average='weighted')))
        print('召回率: {0:0.10f}'.format(metrics.recall_score(actual, predicted, average='weighted')))
        print('f1-score: {0:.3f}'.format(metrics.f1_score(actual, predicted, average='weighted')))

    def predict(self, text_dir=None, text_string=None, encoding='utf-8'):

        """应用模型预测"""
        vocabulary = ft.readobj(self.vocabulary_data)

        if text_dir:

            tfidf_bunch = vector_space(corpus_dir=text_dir, stop_words=None, vocabulary=vocabulary, encoding=encoding, seg=True, tier=1)

            return list(zip(tfidf_bunch.filenames, self._predict(tfidf_bunch.tdm)))
        elif text_string:
            from tfidf_feature import tokenizer
            corpus = [' '.join(tokenizer().cut(text_string))]
            vectorizer = TfidfVectorizer(vocabulary=vocabulary)
            tdm = vectorizer.fit_transform(corpus)
            return self._predict(tdm)
        else:
            return None



