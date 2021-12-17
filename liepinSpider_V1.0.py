# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:52:03 2021

Liepin Spider v1.0

@author: Jacob Qiu
"""


from functions import getHtml

targetAddress = 'https://www.liepin.com/zhaopin/?dq=250070&key=%E6%8B%9B%E8%81%98' 
# 这里后面需要改成input手动传入
output = getHtml(targetAddress)

# 用BeautifulSoup将html格式化
from bs4 import BeautifulSoup as bf
obj = bf(output,'html.parser')
str_obj = str(obj)

# 打开文件
searchResult = open('originalData/Liepin_positionList.txt','w+') # 文件命名可以为‘搜索时间SearchResult’
# 写入，关闭
searchResult.write(str_obj) # 这里边传进来的东西要变
searchResult.close()


from functions import wordTOhtml