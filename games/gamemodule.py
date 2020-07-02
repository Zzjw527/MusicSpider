# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:00:36 2019

@author: hp
"""

from tkinter import *
def gamegame():
    root =Toplevel()
    texlLable = Label(root,text="游戏还在开发中....")
    texlLable.pack(side=LEFT)
    
    photo = PhotoImage(file=r"C:\Users\hp\Desktop\text\game\4499633_233321330321_2.gif")
    img=Label(root,image=photo)
    img.pack(side=RIGHT)
    mainloop()
    
