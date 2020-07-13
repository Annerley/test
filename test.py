import math

def arithmetic(x, y, oper):
    if(oper == '+'):
        return x + y
    elif (oper == '-'):
        return x - y
    elif (oper == '*'):
        return x * y
    elif (oper == '/'):
        return x / y
    else:
        return "Incorrect operation"



def is_year_leap(year):
    if(year % 4 == 0):
        return True
    else:
        return False


def square(side):
    res = (side * 4, side * 2, math.sqrt(2) * side)
    return res

def season(month):
    if((month >= 1 and month < 3) or month ==12):
        return "Winter"
    elif (month > 2 and month <6):
        return "Spring"
    elif (month >5 and month <9):
        return "Summer"
    elif (month >8 and month <12):
        return "Autumn"
    # тут какой-нибудь условный exception

def bank(a, years):
    for i in range(years):
        a+= a*0.1
    return a

def is_prime(b):
    n = 1000
    l = list(range(n))
    l[1] = 0
    for i in l:
        if i > 1:
            for j in range(i+i, len(l), i):
                l[j]=0
    if(l[b]==0):
        return False
    else:
        return True

def date (day, month, year):
    month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                 11: 30, 12: 31
                 }
    if year % 4 ==0:
        month_day[2] = 29
    res = month_day[month]
    if(day <= res):
        return True
    else:
        return False

