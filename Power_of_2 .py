import sys
from sys import argv
Number=int(sys.argv[1])
if(Number<= 31):
    for x in range(0,Number+1):
        power=pow(2,x)
        print("{}".format(power))