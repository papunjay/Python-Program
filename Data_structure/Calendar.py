def isLeapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def week_of_day(day,month,year):
    y0=year-(14-month)//12
    x=y0+y0//4 - y0//100 +y0//400
    m0= month+12*((14-month)//12)-2
    d0=(day+x+31*m0//12) % 7
    return d0
year=int(input())
month=int(input())

months=["January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"]
days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result=isLeapyear(year)
if(result==True):
    days[1]=29
    
print("{} {}".format(months[month-1],year))
print("Su  Mo  Tu  We  Th  Fr  Sa")
day=1
count=0
start_day=week_of_day(day,month,year)