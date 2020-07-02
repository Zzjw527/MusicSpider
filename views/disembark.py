# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:57:29 2019

@author: hp
"""
from views.main1 import main2
import tkinter as tk
class MyDialog(tk.Toplevel):
      def __init__(self):
        super().__init__()
        self.title('设置用户信息')
        self.setup_UI()
      def setup_UI(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='账号：', width=8).pack(side=tk.LEFT)
        self.name = tk.StringVar()
        tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)
        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='密码：', width=8).pack(side=tk.LEFT)
        self.passage = tk.IntVar()
        tk.Entry(row2, textvariable=self.passage, width=20).pack(side=tk.LEFT)
        # 第三行
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)
      def ok(self):
        self.userinfo = [self.name.get(), self.passage.get()] # 设置数据
        self.destroy() # 销毁窗口
      def cancel(self):
        self.userinfo = None # 空！
        self.destroy()
    # 主窗
class MyApp(tk.Tk):
      def __init__(self):
        super().__init__()
        self.title('登陆')
        self.name = '5201314'
        self.passage = 5201314
        self.setupUI()
      def setupUI(self):
        
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='账号：', width=8).pack(side=tk.LEFT)
        self.l1 = tk.Label(row1, text=self.name, width=20)
        self.l1.pack(side=tk.LEFT)
        
        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Label(row2, text='密码：', width=8).pack(side=tk.LEFT)
        self.l2 = tk.Label(row2, text=self.passage, width=20)
        self.l2.pack(side=tk.LEFT)
        
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="切换账户", command=self.setup_config).pack(side=tk.LEFT)
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        tk.Button(row3, text="登陆", command=self.main).pack(side=tk.RIGHT)
      
      def main(self):
          main2(aa=self.name,bb=self.passage)
          
      def setup_config(self):        
        res = self.ask_userinfo()        
        if res is None: return        
        self.name, self.passage = res        
        self.l1.config(text=self.name)
        self.l2.config(text=self.passage)
      
      def ask_userinfo(self):
        inputDialog = MyDialog()
        self.wait_window(inputDialog) 
        return inputDialog.userinfo