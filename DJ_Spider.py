# _*_ coding : UTF-8 _*_
# 开发人员："夏沫丶"
# 开发时间： 2020/1/29 13:42
# 文件名称： DJ_Spider.py
# 开发工具： PyCharm
import requests
import os

from bs4 import BeautifulSoup as bs

from lxml import etree

import re

import time


url_list= []
url_list1 = []
# sesson = requests.session()
url0 = 'http://www.dj97.com/xiazaibang'
headers0 = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
response = requests.get(url0,headers=headers0)
response.encoding='utf-8'

html = etree.HTML(response.text)
messages = html.xpath('//*[@id="J_dances"]/tr/td[3]/a')

for item in messages:
    herf = item.get("href")
    url1 = 'http://www.dj97.com'+herf
    print(url1)
    url_list.append(url1)
    time.sleep(0)
    
headers1 = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Referer" : "http://www.dj97.com/xiazaibang"
}
for url in url_list:
    response = requests.get(url,headers=headers1)
    response.encoding='utf-8'
    response_text= response.text
    # print(response.text)
    re_c= re.compile(r"file: '(.*?)',")
    url_c = re_c.search(response_text).group(1)
    # print(url_c)
    url2 = 'http://m.oscaches.com/mp4/djmusic/'+ url_c+'.mp4'
    # 'http://m.oscaches.com/mp4/djmusic/myxc/20150215/26.mp4'
    print(url2)
    url_list1.append(url2)
    time.sleep(0)
# print([s for s in url_list1])
my_folder = "Down"
j = 0
for i in url_list:
    print(f"开始下载{url_list1[j]}的mp4文件，请稍等.....。")
    headers2 = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Referer": f"{i}"
    }
    response = requests.get(url_list1[j],headers=headers2)
    print(url_list1[j])

    if os.path.exists(my_folder):

        with open("Down\\"+f"{j}.mp4", "wb") as f:
            f.write(response.content)
        j += 1
        print('下载完成')
        time.sleep(5)
    else:
        os.mkdir('Down')
        with open("Down\\" + f"{j}.mp4", "wb") as f:
            f.write(response.content)
        j += 1
        print('下载完成')
        time.sleep(5)
