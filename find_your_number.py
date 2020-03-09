import sys
from sys import argv
def Binary(low,high):
    print("your data low={} and high={} is less then {}".format(low,high,high))
    ans=str(input()) 
    if(high-low)==1:
        print(low)
    else:
        if(ans=='yes'):
            mid=(low+(high-low)//2)
            return Binary(low,mid)
        else:
            low=high
            high=low*2
            mid2=(low+(high-low)//2)
            return Binary(low,mid2)

Number=int(sys.argv[1])
result=Binary(0,Number)
print(result)