’’’
视频演示链接：https://b23.tv/av55224540
微信公众号：teamssix
个人博客：www.teamssix.com
’’’

import os
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
home_url ='https://v.qq.com/x/cover/m441e3rjq9kwpsc/m00253deqqo.html'

#爬取每个视频的id
douluohome = requests.get(home_url,headers=headers)
douluohome.encoding='utf-8'
douluosoup = BeautifulSoup(douluohome.text,'html.parser')
douluolist = douluosoup.select('.mod_episode')[0].select('a')

#合成下载链接
lists = []
for i in range(len(douluolist)):
    lists.append('https://v.qq.com'+douluolist[i]['href'])

#开始下载视频
for i in range(len(lists)):
    try:
        print(os.popen('you-get {}'.format(lists[i])).read()) #视频会下载到当前目录
    except:
        pass
    continue
