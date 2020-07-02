# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:41:11 2019

@author: hp
"""
import requests
import os
import urllib
import json
from tkinter import *
from src.qqmusic import Music
from db_tools.mysql1 import mysqlmysql
from games.gamemodule import gamegame
from games.listenmusic import listen
from tkinter.messagebox import *
from src.translate import translation

import pygame
def main2(aa,bb):    
    aaa=aa
    bbb=bb

    
    def get_real_url(url,try_count = 1):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        dk = response.geturl()
        
        return dk 
    
    def search(self):       
        c=v.get()
        
        
        if c==1:
            global getget
            global mid_list1
            global music_title_list1
            
            lb.delete(0,20)
            get1=e1.get()
            
            getget=Music()
            getget.music1(name=get1)
            mid_list1=getget.mid_list
            music_title_list1=getget.music_title_list
            for key in getget.content:
                lb.insert(END,key)
        if c==2: 
            
            global m_List
            global m_List_id
            global mp3_name
            itemCount = 50
            url = 'http://s.music.163.com/search/get/?type=1&s=%s&limit=%s' % (e1.get(), itemCount)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
            html = requests.get(url, header)
            data = json.loads(html.text)
            m_List = []
            m_List_id=[]
            mp3_name=[]
            try:
                lb.delete(0, lb.size())
                for  musicd in data['result']['songs']:
                    lb.insert(END, musicd['name'] +  '(' + musicd['artists'][0]['name'] + ')')
                    m_List.append(musicd['audio'])
                    m_List_id.append(str(musicd['id']))
                    mp3_name.append(musicd['name']  +'('+ musicd['artists'][0]['name'] + ')')
            except Exception as e:
                print(e)
           
        
    def down(event):
        c=v.get()
        if c==1:
                        
            temp1=lb.get(lb.curselection())
            temp2=temp1[3:4]
            
            ff=mysqlmysql(aaa,bbb,temp2)
            if ff!=1:
                key=list(lb.curselection())
                key.reverse() 
                for index in key:
                    getget.down_music(mid_list1,(index+1),music_title_list1) 
            else:
                answer()
        if c==2:
            de = lb.curselection()[0]
            abspath = os.path.abspath('.')  # 获取绝对路径
            os.chdir(abspath)
            musicurl =get_real_url("http://music.163.com/song/media/outer/url?id="+m_List_id[int(de)]+".mp3")
            
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
            name_cd=mp3_name[int(de)]
            response = requests.get(musicurl, headers=header).content
            path = os.path.join(abspath, name_cd)
            with open(name_cd + '.mp3', 'wb') as f:
                f.write(response)
                print('下载完毕')
                
    def down1(event):         
        key=list(lb.curselection())
        key.reverse() 
        for index in key:
            getget.down_music(mid_list1,(index+1),music_title_list1)        
            
    def gamegamegame(self):
         gamegame()
       
    def musicplay(self):
        listen()
      
    def answer():
        showinfo("下载提示", "这首歌已被下载过咯，重复下载可按其下按钮")
     
    
    def translate(self):
        get2=e2.get()
        translation(ss=get2)
    master=Tk()
    master.geometry("600x400")
    master.title("zjw播放器")
        
    l_show1=Label(master,text="歌曲名字")
    l_show1.grid(row=0,column=0)
    l_show2=Label(master,text="基础功能")
    l_show2.grid(row=20,column=0)
    l_show3=Label(master,text="听厌了歌曲？")
    l_show3.grid(row=30,column=0)
    l_show4=Label(master,text="其他功能")
    l_show4.grid(row=50,column=0)
    l_show5=Label(master,text="看不懂？翻译一下")
    l_show5.grid(row=60,column=0)     
    
    e1 = Entry(master,width=50)
    e1.grid(row=0,column=1)
    e1.delete(0,END)
    e1.insert(0,"请输入歌曲")
    e2 = Entry(master,width=50)
    e2.grid(row=60,column=1)
    e2.delete(0,END)
    e2.insert(0,"请输入要翻译内容")
        
    
    group=LabelFrame(master,text="从哪里搜索？",padx=5,pady=5)
    group.grid(row=5,column=0,padx=1,pady=0)
    
    
    LANGS = [
            ("QQ音乐",1),
            ("网易云音乐",2),
            ]
        
    
    v=IntVar()
    v.set(1)
    for lang, num in LANGS:
        b=Radiobutton(group,text=lang,variable=v,value=num)
        b.pack(anchor = W)    
    sb= Scrollbar(master)
    sb.grid(row=5,column=2,sticky='ns')
        
    lb=Listbox(master,width=50,selectmode = MULTIPLE,yscrollcommand=sb.set)
        
        
        
        
    lb.grid(row=5,column=1)
    sb.config(command=lb.yview)
        
    thebutton1=Button(master,width=8,text="搜索一下")
    thebutton1.bind('<Button-1>',search)
    thebutton1.grid(row=0,column=2)
         
    thebutton2=Button(master,width=10,text="播放")
    thebutton2.bind('<Button-1>',musicplay)
    thebutton2.grid(row=20,column=1,pady=5)
        
    thebutton3=Button(master,width=10,text="立即下载")
    thebutton3.bind('<Button-1>',down)
    thebutton3.grid(row=20,column=2)
        
        
    thebutton4=Button(master,width=10,text="打会儿飞机吧")
    thebutton4.bind('<Button-1>',gamegamegame)
    thebutton4.grid(row=30,column=1)
        
    thebutton5=Button(master,width=10,text="贪吃蛇")
    thebutton5.bind('<Button-1>',gamegamegame)
    thebutton5.grid(row=30,column=2)    
        
    thebutton6=Button(master,width=10,text="重复下载")
    thebutton6.bind('<Button-1>',down1)
    thebutton6.grid(row=50,column=1)
    
    thebutton7=Button(master,width=10,text="批量下载")
    thebutton7.bind('<Button-1>',down1)
    thebutton7.grid(row=50,column=2)    
    
    thebutton8=Button(master,width=10,text="翻译")
    thebutton8.bind('<Button-1>',translate)
    thebutton8.grid(row=60,column=2)    
    
    
          
            
    
     
    
    thebutton1=Button(master,width=8,text="搜索一下")
    thebutton1.bind('<Button-1>',search)
    thebutton1.grid(row=0,column=2)
    
    master.mainloop()