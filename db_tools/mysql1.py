# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:56:40 2019

@author: hp
"""

import pymysql
def mysqlmysql(accountsnum,passwordnum,namenum):
    db = pymysql.connect(
      host="localhost",
      port=3306,
      user="root",
      passwd="123456",
      db="zjw",
      charset='utf8'
      )
    
    cursor= db.cursor()
    sql1='CREATE TABLE IF NOT EXISTS  new_t(id INT AUTO_INCREMENT PRIMARY KEY,accounts INT NOT NULL,password INT NOT NULL,name VARCHAR(255) NOT NULL)' 
    
    b=0
    accounts1=accountsnum
    password1=passwordnum
    name1=namenum
    cursor.execute(sql1)
    cursor.execute('SELECT name FROM new_t')
    myresult =cursor.fetchall()
    for i in myresult:
        
        if i!=name1:
            b=0
        else:
            b=1
            break
        
    if b!=1:
        sql3='INSERT INTO new_t(accounts,password,name) values(%s,%s,%s)'
        cursor.execute(sql3,(accounts1,password1,name1))
        db.commit()   
        db.close()
    return b