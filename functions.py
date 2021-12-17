# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:28:56 2021

Fuctions

@author: Jacob Qiu
"""

import random
import urllib.request
import urllib.parse
import re


def getHtml(targetAddress):
    list_userAgent = ['Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)', 
               'Mozilla/5.0 (compatible; U; ABrowse 0.6;  Syllable) AppleWebKit/420+ (KHTML, like Gecko)', 
               'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)', 
               'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR   3.5.30729)', 
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0;   Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;   SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)', 
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)', 
               'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1;   .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)', 
               'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)', 
               'Mozilla/4.0 (compatible; Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729); Windows NT 5.1; Trident/4.0)', 
               'Mozilla/4.0 (compatible; Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727); Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; .NET CLR 1.1.4322; InfoPath.2)', 
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)']
    u = random.randint(0,len(list_userAgent)-1)
    userAgent = list_userAgent[u]
    #print(userAgent)
    cookie = 'acw_tc=2760823516338607076621711ee440d018c1dd64893f40e30ae5162624d351; \
             Hm_lvt_f3c5c9ab40800b1142160abc4bba3ecb=1633856586,1633860707; \
             Hm_lpvt_f3c5c9ab40800b1142160abc4bba3ecb=1633860707'
    headers = {'User-Agent': userAgent,
               'Connection': 'keep-alive',
               'Cookie': cookie}  
    url = urllib.request.Request(targetAddress,headers=headers)
    pageContent = urllib.request.urlopen(url).read()
    # pageContent = pageContent.decode('UTF-8')
    return pageContent


def wordTOhtml(cnString,salt):
    newString = urllib.parse.quote('%s'%(cnString))
    pattern_newString = re.compile(r'\%')  
    replaceWord = '%' + salt
    htmlString = re.sub(pattern_newString, replaceWord, newString, count=0)
    return htmlString
