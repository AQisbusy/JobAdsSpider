# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:52:03 2021

Liepin Spider demo

@author: Jacob Qiu
"""


from functions import getHtml
from functions import wordTOhtml
import re

cnString = input('Please input the position you want to search for:')
salt = ''

targetPosition = wordTOhtml(cnString, salt)
targetAddress = 'https://www.liepin.com/zhaopin/?headId=66a3abbe5f0dde32b6e5ff8d343a5dac&ckId=66a3abbe5f0dde32b6e5ff8d343a5dac&key=%s&dq=250070&currentPage=0'%(targetPosition)
# 这里后面需要改成input手动传入
output = getHtml(targetAddress)

# 用BeautifulSoup将html格式化
from bs4 import BeautifulSoup as bf
obj = bf(output,'html.parser')
str_obj = str(obj)

'''
# 打开文件
searchResult = open('pageAnalysis/Liepin_positionList.txt','w+') # 文件命名可以为‘搜索时间SearchResult’
# 写入，关闭
searchResult.write(str_obj) # 这里边传进来的东西要变
searchResult.close()
'''


pattern_companyName = re.compile(r'<span class="company-name ellipsis-1">(.*?)</span>')
companyName = re.findall(pattern_companyName, str_obj)
#print(companyName)
print(len(companyName))

pattern_jobTitle = re.compile(r'<div class="ellipsis-1" title="(.*?)">')
jobTitle = re.findall(pattern_jobTitle, str_obj)
print(jobTitle)
print(len(jobTitle))

pattern_salaryRange = re.compile(r'<span class="job-salary">(.*?)</span>')
salaryRange = re.findall(pattern_salaryRange, str_obj)
print(salaryRange)
print(len(salaryRange))

pattern_workLocation = re.compile(r'<span class="ellipsis-1">(.*?)</span>')
workLocation = re.findall(pattern_workLocation, str_obj)
#print(workLocation)
print(len(workLocation))



'''
#公司规模、行业有缺失值
pattern_companyIndustryFinSize = re.compile(r'<div class="company-tags-box ellipsis-1">(\n*.*?)\n</div>')
companyIndustryFinSize = re.findall(pattern_companyIndustryFinSize, str_obj)
print(companyIndustryFinSize)
print(len(companyIndustryFinSize))
'''



'''
#招聘要求和岗位关键词现在混在一起
pattern_experienceReq = re.compile(r'<span class="labels-tag">(.*?)</span>')
experienceReq = re.findall(pattern_experienceReq, str_obj)
print(experienceReq)
print(len(experienceReq))
'''

