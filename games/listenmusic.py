# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:00:24 2019

@author: hp
"""


from tkinter import *
def listen():
    root =Toplevel()
    texlLable = Label(root,text="请自行下载后到文件夹中打开吧")
    texlLable.pack(side=LEFT)
    
    photo = PhotoImage(file=r"C:\Users\hp\Desktop\text\game\5cadecc29ef0e_preview.gif")
    img=Label(root,image=photo)
    img.pack(side=RIGHT)
    mainloop()