# -*- coding: utf-8 -*-
"""
Created on Sat OCT 23 18:28:06 2021

51 Job Spider v1.2

@author: Jacob Qiu
"""


from functions import getHtml
from functions import wordTOhtml
import re
import pandas as pd
import time
import random

#预设内容
cnString = input('Please input the position you want to search for:')
salt = '25'
startPage = 1
endPage = 9999 # 默认放在1和9999就可以了，有指定的页码范围要爬的时候再改



targetPosition = wordTOhtml(cnString, salt)
for p in range(startPage,endPage+1):
    targetAddress = 'https://search.51job.com/list/120000,000000,0000,00,9,99,%s,2,%d.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='%(targetPosition, p)
    output = getHtml(targetAddress)

    st = random.randint(1,10)
    time.sleep(st)
    
    # 用BeautifulSoup将html格式化
    from bs4 import BeautifulSoup as bf
    obj = bf(output,'html.parser')
    str_obj = str(obj)
    #print(type(obj))
    #print(str_obj)
    
    # 打开文件
    # searchResult = open('C:/Users/qiuti/Desktop/51jobSpyder/originalData/originalData_positionList.txt','w+')
    # 写入，关闭
    # searchResult.write(str(positionList1))
    # searchResult.close()
    
    
    # 获取职位列表
    pattern_positionList = re.compile(r'window.__SEARCH_RESULT__ = {(.*)}')
    positionList = re.findall(pattern_positionList, str_obj)
    #str_positionList = str(positionList)
    #print(len(str_positionList))
    #print(positionList)
    #print(type(positionList))
    #print(len(positionList))
    #string_positionList = positionList[0]
    #print(string_positionList)
    #print(len(string_positionList))
    print('Processing...')
    
    # 输出公司名称&判断页面是否为空
    pattern_companyName = re.compile(r'"company_name":"(.*?)"')
    companyNameText = re.findall(pattern_companyName, str(positionList))
    # print(companyName)
    # print(len(companyName))
    # print(type(pattern_companyName))
    if len(companyNameText) == 0:
        #print('fail')
        break
    else:
        #print('Pass')
    
        # 输出公司性质
        pattern_companytypeText = re.compile(r'"companytype_text":"(.*?)"')
        companytypeText = re.findall(pattern_companytypeText, str(positionList))
        # print(companytypeText)
        # print(len(companytypeText))
        
        
        # 输出公司规模
        pattern_companysizeText = re.compile(r'"companysize_text":"(.*?)"')
        companysizeText = re.findall(pattern_companysizeText, str(positionList))
        # print(companysizeText)
        # print(len(companysizeText))
        
        
        # 输出岗位名称
        pattern_jobName = re.compile(r'"job_name":"(.*?)"')
        jobNameText = re.findall(pattern_jobName, str(positionList))
        # print(jobName)
        # print(len(jobName))
        
        
        # 输出工作地点
        pattern_workareaText = re.compile(r'"workarea_text":"(.*?)"')
        workareaText = re.findall(pattern_workareaText, str(positionList))
        # print(workareaText)
        # print(len(workareaText))
        
        
        # 输出薪资范围--“/月”那里还需要再清洗一下
        pattern_providesalaryText = re.compile(r'"providesalary_text":"(.*?)"')
        providesalaryText = re.findall(pattern_providesalaryText, str(positionList))
        #print(providesalaryText)
        #print(len(providesalaryText))
        
        
        # 输出福利
        pattern_benefitText = re.compile(r'"jobwelf_list":\[(.*?)\]')
        benefitsText = re.findall(pattern_benefitText, str(positionList))
        #print(benefitText)
        #print(len(benefitText))
        
        
        # 输出学历要求、工作年限要求、招聘人数--都藏在attribute_text里面，需要再清洗一下
        pattern_attributeText = re.compile(r'"attribute_text":\[(.*?)\]')
        attributeText = re.findall(pattern_attributeText, str(positionList))
        #print(attributeText)
        #print(len(attributeText))
        
     
        # 获取的数据写入excel文件
        #targetInfo = ['公司名称','公司性质','岗位名称','薪资范围','工作地点']
        dataframe = pd.DataFrame({'公司名称':companyNameText,
                                  '公司性质':companytypeText,
                                  '公司规模':companysizeText,
                                  '岗位名称':jobNameText,
                                  '工作地点':workareaText,
                                  '薪资范围':providesalaryText,
                                  '公司福利':benefitsText,
                                  '其他信息':attributeText})
        dataframe.to_excel('data/%s_Page%d.xlsx'%(cnString, p),encoding='utf-8')

print('Done!')
