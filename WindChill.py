import sys
import math 
from sys import argv
t=float(sys.argv[1])
v=float(sys.argv[2])
if(t<=50 and (v<=120 and v>=3)):
    w=35.74+0.6215*t + (0.4275*t - 35.75)* math.pow(v,0.16)
    print(w)
else:
    print("Enter Valid data")
    