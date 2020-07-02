# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:53:24 2019

@author: hp
"""

from views.main import startstart

if __name__ == '__main__':
    startstart()
    
    
"""
播放器/
|-- views/               界面
|   |-- __init__.py
|   |-- main.py          程序运行主体程序1
|   |-- main1.py         程序运行主体程序2
|   |-- disembark.py     实现登陆界面

|-- game/                游戏
|   |-- __init__.py
|   |-- gamemodel.py     游戏模块
|   |-- listenmusic.py   音乐播放模块
|   |-- image            图片

|-- db_tools/            MySQL数据库
|   |-- __init__.py
|   |-- mysql1.py        实现数据导入数据库和防止重复下载功能

|-- src/                 爬虫文件
|   |-- __init__.py 
|   |--qqmusic.py        爬取qq音乐
|   |--translate.py      爬取有道翻译
|   |--wangyiyun.py      爬取网易云音乐


|-- start.py           程序启动文件
|-- README.md           程序使用说明
|-- 优缺点.word           优缺点

"""