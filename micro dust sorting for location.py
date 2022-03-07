import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import Juliancalculator as JJ


data_origin = pd.read_csv('micro dust.csv',encoding='CP949')
data = data_origin.drop(['Unnamed: 0','time'],axis=1)

# ####
# data_mean = data[data['location'] == '강남구']
# data_mean = data_mean[(JJ.Juliancal(2020,1,1,0) < data_mean['julian_date']) &
#                       (data_mean['julian_date'] < JJ.Juliancal(2020,2,1,0))]
# plt.plot(data_mean['julian_date'],data_mean['PM10'],'r-',data_mean['julian_date'],data_mean['PM2.5'])
# plt.show()
# ###


E = ['강북구','도봉구','노원구','중랑구','광진구','성동구','동대문구','성북구']
W = ['강서구','양천구','구로구','영등포구','금천구','관악구','동작구']
N = ['은평구','마포구','서대문구','종로구','중구','용산구']
S = ['서초구','강남구','송파구','강동구']
evg = ['평균']
columns = ['강동','강서','강북','강남','평균']

E.sort()
W.sort()
N.sort()
S.sort()

loc_list = pd.DataFrame([E,W,N,S,evg])
loc_list = loc_list.T
loc_list.columns = columns
loc_list = loc_list.fillna('    x  ')
# print(loc_list)

find = W
for v in find:
    mask = data[data['location'] == v]
    mask = mask.set_index('julian_date')
    if v == find[0]:
        df = mask
    else:
        df = pd.concat([df,mask],axis=1)
df = df.drop('location',axis=1)
df.columns = list(np.arange(len(find)*2)+1)
# odd : PM10 , even : PM2.5


