"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2020/3/6 10:57

"""

import pandas as pd
import numpy as np
import math

resident=pd.read_excel(r"C:\Users\Dell\Desktop\龙岩现状模型\新建文件夹\Resident.xlsx")
employ=pd.read_excel(r"C:\Users\Dell\Desktop\龙岩现状模型\新建文件夹\employ.xlsx")
# print(resident)

dict={} #用于存放小区的平均出行距离
# print(resident.loc[0:1,'Rx'])
distance=[0 for i in range(len(resident))]
new_res=resident.copy()  #复制一个dataframe
new_res['distance']=distance

# for i in range(0,len(resident)):
#     new_res[i,'distance']=i
# print('done')
def calcdist(Ex,Rx,Ey,Ry):
    dist=math.sqrt(pow(Rx-Ex,2)+pow(Ry-Ey,2))
    return dist
# print(calcdist(1,2,2,3))   #test
#两个循环,对应着居住区和就业区的zoneid
# zoneid=resident['ZONEID'][0:3]       #选取某一列中具体某个值
rows_res=len(resident)   #居住dataframe行数
rows_emp=len(employ)  #工作dataframe行数
for i in range(0,rows_res):
    zoneid_res=resident['ZONEID'][i]
    Rx=resident['Rx'][i]
    Ry=resident['Ry'][i]
    avrg_dist=[]  #创建临时列表，用于求小区出行距离平均值
    for j in range(0,rows_emp):
        zoneid_emp=employ['ZONEID'][j]
        Ex=employ['Ex'][j]
        Ey=employ['Ey'][j]
        print(zoneid_res,zoneid_emp)
        if  zoneid_res==zoneid_emp:
            dist=calcdist(Ex,Rx,Ey,Ry)
            avrg_dist.append(dist)    #若改进，需加上对应的权重
            new_res.loc[i,'distance']=np.mean(avrg_dist)
            print(np.mean(avrg_dist))
    print("第"+str(i)+"小区计算完成")
print('done!')

new_res.to_excel(r"C:\Users\Dell\Desktop\龙岩现状模型\新建文件夹\new_res.xlsx")
















