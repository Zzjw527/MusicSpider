# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:17:09 2019

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:31:53 2019

@author: hp
"""
import http.cookiejar
import re
import json
import requests
import os
def get_real_url(url,try_count = 1):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    dlink = response.geturl()
    print(dlink)
    return dlink
def music(name):
    itemCount = 50
    url = 'http://s.music.163.com/search/get/?type=1&s=%s&limit=%s' % (name,itemCount)
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    html = requests.get(url, header)
    data = json.loads(html.text)
    m_List = []
    m_List_id=[]
    mp3_name=[]
    for music in data['result']['songs']:
            
            m_List.append(music['audio'])
            m_List_id.append(str(music['id']))
            mp3_name.append(music['name'] + '------' +'('+ music['artists'][0]['name'] + ')')
            print(music['name'] + '--' +  music['artists'][0]['name'] )
            print('id:'+m_List_id[0])
    tt=input("请复制粘贴你想要下载的歌曲id:")
    down_music(tt,name)
            


def down_music(tt,name_cd):
    abspath = os.path.abspath('.')  # 获取绝对路径
    os.chdir(abspath)
    musicurl =get_real_url("http://music.163.com/song/media/outer/url?id="+tt+".mp3")
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    
    response = requests.get(musicurl, headers=header).content
    path = os.path.join(abspath, name_cd)
    with open(name_cd + '.mp3', 'wb') as f:
        f.write(response)
        print('下载完毕')



if __name__ == "__main__":
    name = input("请输入要下载的歌名\n>>> ")
    music(name=name)
