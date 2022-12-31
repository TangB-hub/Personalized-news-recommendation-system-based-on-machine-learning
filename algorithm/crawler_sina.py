from importlib import reload

import requests
from bs4 import BeautifulSoup
import time
import json
import re
import pandas
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
def getnewcontent(url):
    filename='./content/'
    result = {}
    info = requests.get(url)
    info.encoding = 'utf-8'
    html = BeautifulSoup(info.text, 'html.parser')
    result['title'] = html.select('.second-title')[0].text
    result['date'] = html.select('.date')[0].text
    result['source'] = html.select('.source')[0].text
    result['link'] = html.select('.source')[0].get('href')


    article = []
    for v in html.select('.article p')[:-1]:

        article.append(v.text.strip())

    author_info = '\n'.join(article)
    result['content'] = author_info

    result['author'] = html.select('.show_author')[0].text.lstrip('责任编辑：')

    return result

def getnewslink(url):
    test = requests.get(url)
    test2 =  test.text.lstrip('newsloadercallback(')
    jd = json.loads(test2.rstrip(')\n'))
    content = []
    for v in jd['result']['data']:
        content.append(getnewcontent(v['url']))

    return content
def getdata():
    url = 'https://interface.sina.cn/news/get_news_by_channel_new_v2018.d.html?cat_1=51923&show_num=27&level=1,2&page={}&callback=newsloadercallback&_=1536044408917'
    weibo_info = []
    for i in range(1,6):
        newsurl = url.format(i)#字符串格式化用i替换{}
        weibo_info.extend(getnewslink(newsurl))
    return weibo_info

new_info = getdata()
df = pandas.DataFrame(new_info)
filename='./news/'
df.to_excel(filename+'sinanews.xlsx')
#去除全部 df.head() 取出5行 head(n)  n行
#将文件下载为excel表格 df.to_excel('weibonews.xlsx')