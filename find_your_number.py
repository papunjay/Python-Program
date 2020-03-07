import sys
from sys import argv
def Binary(Number,start,end):
    mid=start+(end-start)//2
    print(mid)
Number=int(sys.argv[1])
Binary(Number,0,Number)