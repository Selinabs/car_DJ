# _*_ coding : UTF-8 _*_
# 开发人员："夏沫丶"
# 开发时间： 2020/1/29 14:04
# 文件名称： test.py
# 开发工具： PyCharm
import requests
import re
from lxml import etree
#
# url = "http://www.dj97.com/xiazaibang"
# ak = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
# }
# response = requests.get(url, headers=ak)
# response.encoding = 'utf-8'
# response = response.text
# # dj_url_list = re.compile(r'/xiazaibang/(.*?)">2</a>')
# # dj_url1 = "http://www.dj97.com/xiazaibang"
# html = etree.HTML(response)
# dj_url= html.xpath('//*[@id="J_DN92116"]/text()')
# print(dj_url)
url = 'http://www.dj97.com/xiazaibang/m/92116/'
headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
response = requests.get(url,headers=headers)

response.encoding='utf-8'

print(response.text)