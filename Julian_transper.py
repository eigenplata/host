import Juliancalculator as JJ
import sys

print('날짜를 입력하세요. \t ex)20220301')

try:
    
    date = input()

    if len(date)>8:
        raise ValueError
    
except ValueError:
    print('날짜를 잘못 입력했습니다.')
    sys.exit()
    

print('혹시 시간도 필요하신가요? \n필요하다면 입력해주시고 아니면 0을 입력해주세요. \t ex)13시: 13')
hour = int(input())
year = int(date[:4])
month = date[4:6]
day = date[-2:]

if month[0] == '0':
    month = int(month[1])
else:
    month = int(month)
    
if day[0] == '0':
    day = int(day[1])
else:
    day = int(day)
    
J = JJ.Juliancal(year, month, day, hour)
print('입력하신 날짜는 {0}.{1}.{2}.{3}시'.format(year, month, day, hour))
print('\nJulian date: {}'.format(J))

[y,m,d] = JJ.Juliancal_reverse(J)

print('reverse: {0}.{1}.{2}.{3}시'.format(y,m,d,hour))

yr = JJ.Julian_year_reverse(J)
mr = JJ.Juliancal_month_reverse(J)
dr = JJ.Juliancal_day_reverse(J)

print('reverse Unit: {0}.{1}.{2}.{3}시'.format(yr,mr,dr,hour))