"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/10/28 9:24

"""

import pandas as pd
import numpy as np

data=pd.read_excel("c:/users/dell/desktop/test.xlsx")
print(data)



# data=pd.DataFrame(data=ws2,index=[[1,2],[1,2,3,4]],columns=[[1,2],[1,2,3,4]])
# data=pd.DataFrame(data=ws2,index=['2','3','4','5'])
# print(data)

# frame=pd.DataFrame(np.arange(12).reshape((4,3)), index=[['a','a','b','b'],[1,2,1,2]],
#   columns=[['Ohio','Ohio','Colorado'],
#   ['Green','Red','Green']])
