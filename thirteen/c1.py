# 明确目的
# 找到数据对应的网页
# 分析网页的结构 找到数据所在的标签位置
# 模拟HTTP请求，向服务器发送请求，获取服务器返回给我们的HTML

from urllib import request
import urllib.request
import re

import requests
import gzip
from bs4 import BeautifulSoup

#腾讯url
tUrl = "https://v.qq.com/x/bu/pagesheet/list?_all=1&append=0&channel=movie&characteristic=5&listpage=2&pagesize=30&sort=18&offset=0"
#tUrl = 'https://v.qq.com/channel/choice?ptag=qqbrowser&ADTAG=zd-tdh&channel_2022=1'

#请求
# ret = requests.get(url=tUrl, stream=True)
# gy_fp = open('html.txt',mode = 'w+',encoding = 'utf-8')
# gy_fp.write(ret.text)
# gy_fp.close()
#print(ret.text)

# def loadUrl(adress): 
#   adress = urllib.unquote(adress)
#   print("Loading " + adress)
#   socket =urllib.urlopen(adress)
#   html = socket.read()
#   socket.close()
#   soup = BeautifulSoup(html)
#   return soup


# soup = loadUrl("http://de.pokerstrategy.com/forum/thread.php?threadid=498111")


 
url = "https://v.qq.com/channel/choice?ptag=qqbrowser&ADTAG=zd-tdh&channel_2022=1"
response1 = urllib.request.urlopen(url)
print("第一种方法")
#获取状态码，200表示成功
print(response1.getcode())
#获取网页内容的长度
htmls = response1.read()
htmls_str = htmls.decode('utf-8')
print(len(htmls))
#htmls_str = str(htmls,encoding = 'utf-8')
gy_fp = open('html.txt',mode = 'w+',encoding = 'utf-8')
gy_fp.write(htmls_str)
gy_fp.close()

class Spider():
    gy_url = 'https://v.qq.com/channel/choice?ptag=qqbrowser&ADTAG=zd-tdh&channel_2022=1'
    gy_root_pattern = '<div class="nowpc-activity-business-InfoCard__base-info">[\s\S]*?</div>'
    gy_title_pattern = '<span>[\s\S]*?</span>'

    def __fetch_content(self):
        result = request.urlopen(Spider.gy_url)
        htmls = result.read()
        print(type(htmls))
        #print(htmls)
        #htmls_str = htmls.decode('UTF-8')
        htmls_str = str(htmls,encoding = 'utf-8')
        #gy_fp = open('html.txt',mode = 'w+',encoding = 'utf-8')
        #gy_fp.write(htmls_str)
        #print(htmls_str)
        gy_b = 1
        return htmls_str

    def __analysis(self,htmlstring):
        gy_root_html = re.findall(Spider.gy_root_pattern,htmlstring)
        print(list(gy_root_html))
        gy_a = 1

    def spider_go(self):
        htmls_string = self.__fetch_content()
        self.__analysis(htmls_string)


#gy_spider = Spider()

#gy_spider.spider_go()


















