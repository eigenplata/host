import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Juliancalculator import Juliancal as JJ



data = pd.read_csv('Origin.csv',encoding='CP949')
# data = pd.read_csv('Origin_1.csv',encoding='UTF-8')

date = data['일시']

date = date.apply(lambda v: v.replace('-', ' ')) #연도 달 날짜 
date = date.apply(lambda v: v.replace(':', ' ')) # 시간
date = pd.DataFrame(date.apply(lambda v: v.split()[:4]).tolist(),
                    columns = ('year','month','day','hour'))

date['month'] = date['month'].apply(lambda v: v[1] if v[0]=='0' else v)
date['day'] = date['day'].apply(lambda v: v[1] if v[0]=='0' else v)

date = date.astype(int)

data['julian_date'] = date.apply(lambda v: JJ(v['year'], v['month'], v['day'], v['hour']), axis=1)

# print(data)

# data.to_csv('before sort.csv',encoding='CP949')

data['미세먼지(PM10)'] = data['미세먼지(PM10)'].fillna(data['미세먼지(PM10)'].mean())
data['초미세먼지(PM25)'] = data['초미세먼지(PM25)'].fillna(data['초미세먼지(PM25)'].mean())
data = data[['julian_date', '구분', '미세먼지(PM10)', '초미세먼지(PM25)','일시']]
data = data.rename(columns = {'구분':'location', '미세먼지(PM10)':'PM10', '초미세먼지(PM25)':'PM2.5','일시':'time'})

data_sort = data.sort_values('julian_date')


data_sort.to_csv('micro dust.csv', encoding = 'CP949')

# plt.plot(data_final['julian_date'], data_final['PM10'])
# plt.show()

# data_gangnam = data_final[data_final['location'] == '평균']
# # print(data_gangnam)