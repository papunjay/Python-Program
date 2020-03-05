import sys
from sys import argv
week=['Sunday','Monday','Tuseday','Wednesday','Thursday','Friday','Saturday']
month=int(argv[1])
day=int(argv[2])
year=int(argv[3])
y0=year-(14-month)//12
x=y0+y0//4 - y0//100 +y0//400
m0= month+12*((14-month)//12)-2
d0=(day+x+31*m0//12) % 7
print(week[d0])

