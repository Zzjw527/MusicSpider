# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:44:21 2019

@author: hp
"""
import re
import json
import requests
class Music():
    def __init__(self):
        self.content=[]
        self.mid_list=[]
        self.music_title_list=[]
    def music1(self,name):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url =f"https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=62115878671550904&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={name}&g_tk=5381&jsonpCallback=MusicJsonCallback2806001545440244&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                json_list = requests.get(url,headers=headers).text        
                res = re.compile(r"MusicJsonCallback.*?{(.*)}", re.S)
                self.content = re.findall(res, json_list)
                content_1 = '{'+self.content[0]+'}'
                dict_content = json.loads(content_1)
                self.content=[]
                keyword = dict_content["data"]["keyword"]
                list_all = dict_content["data"]["song"]["list"]
                
                for index, for_dict in enumerate(list_all):
                   
        
                    album_name = for_dict["album"]["title"]
        
                    self.mid_list.append(for_dict["mid"])
        
                    self.music_title = for_dict["title"]
                    self.music_title_list.append(self.music_title)
        
                    singer_name = for_dict["singer"][0]["title"]
                    self.content.append([ index + 1,self.music_title,singer_name,album_name])
        except requests.RequestException:
                print("网络未连接或出错")
                return None
    def down_music(self,mid_list, number, music_title_list):
       
        url = f"https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey12314283393950355&g_tk=5381&jsonpCallback=getplaysongvkey12314283393950355&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22req_0%22:%7B%22module%22:%22vkey.GetVkeyServer%22,%22method%22:%22CgiGetVkey%22,%22param%22:%7B%22guid%22:%224357915898%22,%22songmid%22:[%22{mid_list[number-1]}%22],%22songtype%22:[0],%22uin%22:%220%22,%22loginflag%22:1,%22platform%22:%2220%22%7D%7D,%22comm%22:%7B%22uin%22:0,%22format%22:%22json%22,%22ct%22:20,%22cv%22:0%7D%7D"
    
        join_url = requests.get(url).text
        res = re.compile(r"getplaysongvkey.*?{(.*)}", re.S)
        url_content = re.findall(res, join_url)
        char_url = "{" + url_content[0] + "}"
        dict_url = json.loads(char_url)
        finally_url = "http://111.7.162.144/amobile.music.tc.qq.com/" + dict_url["req_0"]["data"]["midurlinfo"][0]["purl"]
        name_cd = music_title_list[number - 1]
        print(name_cd+" =>正在下载中....")
        
        with open(name_cd + ".mp3", "wb")as musicopen:
            musicopen.write(requests.get(finally_url).content)
        print("歌曲已下载成功！")
    

