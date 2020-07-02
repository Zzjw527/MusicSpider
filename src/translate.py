# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:56:43 2019

@author: hp
"""

import urllib.request
import urllib.parse
import json
def translation(ss):
    content = ss
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='15522091177102'
    data['sign']='705f5ea569b2b39e006b96372805b830'
    data['ts']='1552209117710'
    data['bv']='d37709c74ef1702ea7c1f7a04a06c36e'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_REALTIME'
    data['typoResult']='false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    
    T = json.loads(html)
    print("翻译结果：%s"%(T['translateResult'][0][0]['tgt']))


