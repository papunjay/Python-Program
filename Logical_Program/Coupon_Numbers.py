import random
from array import *
arr=array('i',[])
# print the output
def print_function(arr,Number,count):
    print("number of iterations required={}".format(count))
    for i in range(Number):
        print( arr[i])
# stor the dist value in array
def Dist_value(Number):
    count=0
    size=0
    
    while True:
        dist_Number=random.randint(1,100)
        count=count+1
        if(size!=Number):
            duplicate=0
            for i in range(size):
                if(dist_Number==arr[i]):
                    duplicate+=1
            if(duplicate==0):
                arr.append(dist_Number)
                size+=1
        else:
            break
    print_function(arr,Number,count)
#main
Number=int(input("Enter the total Number..."))
Dist_value(Number)
