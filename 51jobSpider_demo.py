# -*- coding: utf-8 -*-


import urllib.request
import re
import pandas as pd



# 取url里html内容；加请求头模拟浏览器访问防封
def getHtml(targetAddress):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 \
               Safari/537.36 Edg/91.0.864.37'}  # 视情况决定要不要加cookies
    url = urllib.request.Request(targetAddress,headers=headers)
    pageContent = urllib.request.urlopen(url).read()
    # pageContent = pageContent.decode('UTF-8')
    return pageContent


#url = input('请输入链接：')


targetAddress = 'https://search.51job.com/list/120000,000000,0000,00,9,99,.net,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=' 
# 这里后面需要改成input手动传入
output = getHtml(targetAddress)



# 用BeautifulSoup将html格式化
from bs4 import BeautifulSoup as bf
obj = bf(output,'html.parser')
str_obj = str(obj)
#print(type(obj))
#print(str_obj)

# 打开文件
# searchResult = open('C:/Users/qiuti/Desktop/51jobSpyder/originalData/originalData_positionList.txt','w+') # 文件命名可以为‘搜索时间SearchResult’
# 写入，关闭
# searchResult.write(str(positionList1)) # 这里边传进来的东西要变
# searchResult.close()


# 获取职位列表
pattern_positionList = re.compile(r'window.__SEARCH_RESULT__ = {(.*)}')
positionList = re.findall(pattern_positionList, str_obj)
str_positionList = str(positionList)
#print(positionList)
#print(type(positionList))
#print(len(positionList))
string_positionList = positionList[0]



# 输出公司名称
pattern_companyName = re.compile(r'"company_name":"(.*?)"')
companyName = re.findall(pattern_companyName, str(positionList))
# print(companyName)
# print(len(companyName))
# print(type(pattern_companyName))


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
jobName = re.findall(pattern_jobName, str(positionList))
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
dataframe = pd.DataFrame({'公司名称':companyName,
                          '公司性质':companytypeText,
                          '公司规模':companysizeText,
                          '岗位名称':jobName,
                          '工作地点':workareaText,
                          '薪资范围':providesalaryText,
                          '公司福利':benefitsText,
                          '其他信息':attributeText})
dataframe.to_excel('data/organizedData6.xls',encoding='utf-8')




# company_name -- Done
# companytype_text -- Done
# companysize_text -- Done
# job_name -- Done
# providesalary_text -- Done
# workarea_text -- Done
# attribute_text
# degreefrom
# workyear
# jobwelf_list
# issuedate



'''
def getInfo(targetInfo, positionList):
    pattern = re.compile(r'"%s":"(.*?)"')
    print(pattern)
    contentText = re.findall(pattern, str(positionList))
    return contentText
    return len(contentText)

targetInfo = 'company_name'

#,'companytype_text','companysize_text','job_name','providesalary_text',\
#'workarea_text','degreefrom','workyear','jobwelf_list','issuedate'

A = getInfo(targetInfo, positionList)

print(A)
'''


'''
# 翻页
targetAddress = 'https://search.51job.com/list/120300,000000,0000,00,9,99,.net,2,%d.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='%(pageNum) 
for i in range(1,200):
    if getHtml(targetAddress) > 0:
        pageNum = i
        output = getHtml(targetAddress)
        print(len(output))
        i += 1
    else:
        break
'''










