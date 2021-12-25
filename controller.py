# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:26:43 2021

controller

@author: Jacob Qiu
"""

from typing import Pattern
from prettytable import PrettyTable
import re


# ---------- 51job ----------

# 公司性质, cotype
cotypeList = {
    '99':'全部',
    '01':'外资（欧美）',
    '02':'外资（非欧美）',
    '03':'合资',
    '04':'国企',
    '05':'民营公司',
    '06':'外企代表处',
    '07':'政府机关',
    '08':'事业单位',
    '09':'非盈利组织',
    '10':'上市公司',
    '11':'创业公司'
    }


codes = list(cotypeList.keys())
print(codes)
meanings = list(cotypeList.values())
print(meanings)


cotype = PrettyTable()
cotype.add_column("Code", codes)
#cotype.align["Code"] = "l"
cotype.add_column("Meaning",meanings)
#cotype.align["Meaning"] = "l"
print(cotype)

cotypeCode = '01+02'
print(len(cotypeCode))

pattern_cotypeCode = re.compile(r'\d\d(+)\d\d')
cotypeCode_convert = re.match(cotypeCode, pattern_cotypeCode)
print(cotypeCode_convert)

if len(cotypeCode) == 2:
    cotypeCode = cotypeCode
    print(cotypeCode)
else:
    cotypeCode = cotypeCode_convert
    print(cotypeCode)




# ---------- Liepin ----------