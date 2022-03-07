import math

# xxxx.xx.xx.xx >> xxxxxx.xx

def Juliancal(year,month,day,hour):
    # year
    year_leap = (year - 1) // 4
    J_y = year_leap * 366 + ((year - 1) - year_leap) * 365
    
    # month
    m1 = 0 
    m2 = 31 +m1
    m3 = 28 + m2
    m4 = 31 + m3
    m5 = 30 + m4
    m6 = 31 + m5
    m7 = 30 + m6
    m8 = 31 + m7
    m9 = 31 + m8
    m10 = 30 + m9
    m11 = 31 + m10
    m12 = 30 + m11
    
    m = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    m_l = [m1,m2,m3+1,m4+1,m5+1,m6+1,m7+1,m8+1,m9+1,m10+1,m11+1,m12+1]
    # 2월이 29일인 윤년이 있기 때문에    
    
    if year % 4 == 0 :
        J_m = m_l[month - 1]
    else:
        J_m = m[month - 1]
    
    # day
    J_d = day
    
    #hour
    J_h = hour / 24
    J_h = round(J_h , 2)

    # sum
    J = J_y + J_m + J_d + J_h
    
    return J

def Juliancal_year(year):
    year_leap = (year - 1) // 4
    J_y = year_leap * 366 + ((year - 1) - year_leap) * 365
    
    return J_y

def Juliancal_month(year,month):

    # month
    m1 = 0 
    m2 = 31 +m1
    m3 = 28 + m2
    m4 = 31 + m3
    m5 = 30 + m4
    m6 = 31 + m5
    m7 = 30 + m6
    m8 = 31 + m7
    m9 = 31 + m8
    m10 = 30 + m9
    m11 = 31 + m10
    m12 = 30 + m11
    
    m = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    m_l = [m1,m2,m3+1,m4+1,m5+1,m6+1,m7+1,m8+1,m9+1,m10+1,m11+1,m12+1] 
    
    if year % 4 == 0 :
        J_m = m_l[month - 1]
    else:
        J_m = m[month - 1]
    
    return J_m

def Juliancal_hour(hour):
    J_h = hour / 24
    J_h = round(J_h , 2)

    return J_h


# xxxxxx.xx >> xxxx.xx.xx.xx

def Juliancal_reverse(date):
    # year
    date = math.trunc(date)
    year = 1 + date // 365.25
    year_leap = (year - 1) // 4
    J_y = year_leap * 366 + ((year - 1) - year_leap) * 365
    J_m = date - J_y
    
    # month set
    m1 = 0 
    m2 = 31 +m1
    m3 = 28 + m2
    m4 = 31 + m3
    m5 = 30 + m4
    m6 = 31 + m5
    m7 = 30 + m6
    m8 = 31 + m7
    m9 = 31 + m8
    m10 = 30 + m9
    m11 = 31 + m10
    m12 = 30 + m11
    m = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    m_l = [m1,m2,m3+1,m4+1,m5+1,m6+1,m7+1,m8+1,m9+1,m10+1,m11+1,m12+1]
    
    #month and day
    if year % 4 != 0:
        for i in range(len(m)-1):
            if m[i] < J_m <= m[i+1]:
                month = i+1
                break
        day = J_m - m[i]
    else:
        for i in range(len(m)-1):
            if m_l[i] < J_m <= m_l[i+1]:
                month = i+1
                break
        day = J_m - m_l[i]
        
    
    
    return int(year) , month , int(day)

def Julian_year_reverse(date):
    date = math.trunc(date)
    year = 1 + date // 365.25
    
    return int(year)

def Juliancal_month_reverse(date):
    date = math.trunc(date)
    year = 1 + date // 365.25
    year_leap = (year - 1) // 4
    J_y = year_leap * 366 + ((year - 1) - year_leap) * 365
    J_m = date - J_y
    
    # month
    m1 = 0 
    m2 = 31 +m1
    m3 = 28 + m2
    m4 = 31 + m3
    m5 = 30 + m4
    m6 = 31 + m5
    m7 = 30 + m6
    m8 = 31 + m7
    m9 = 31 + m8
    m10 = 30 + m9
    m11 = 31 + m10
    m12 = 30 + m11
    m = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    m_l = [m1,m2,m3+1,m4+1,m5+1,m6+1,m7+1,m8+1,m9+1,m10+1,m11+1,m12+1]
    
    if year % 4 != 0:
        for i in range(len(m)-1):
            if m[i] < J_m <= m[i+1]:
                month = i+1
                break
    else:
        for i in range(len(m)-1):
            if m_l[i] < J_m <= m_l[i+1]:
                month = i+1
                break
        
    
    
    return month

def Juliancal_day_reverse(date):
    # year
    date = math.trunc(date)
    year = 1 + date // 365.25
    year_leap = (year - 1) // 4
    J_y = year_leap * 366 + ((year - 1) - year_leap) * 365
    J_m = date - J_y
    
    # month
    m1 = 0 
    m2 = 31 +m1
    m3 = 28 + m2
    m4 = 31 + m3
    m5 = 30 + m4
    m6 = 31 + m5
    m7 = 30 + m6
    m8 = 31 + m7
    m9 = 31 + m8
    m10 = 30 + m9
    m11 = 31 + m10
    m12 = 30 + m11
    m = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    m_l = [m1,m2,m3+1,m4+1,m5+1,m6+1,m7+1,m8+1,m9+1,m10+1,m11+1,m12+1]
    
    if year % 4 != 0:
        for i in range(len(m)-1):
            if m[i] < J_m <= m[i+1]:
                break
        day = J_m - m[i]
    else:
        for i in range(len(m)-1):
            if m_l[i] < J_m <= m_l[i+1]:
                break
        day = J_m - m_l[i]
        
    return int(day)











