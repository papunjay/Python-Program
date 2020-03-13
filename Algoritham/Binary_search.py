from array import *
mid_val=0
def Binary_search(arr,l,r,x):
    if r>=l:
        mid_val=l+(r-l)//2
        if(arr[mid_val]==x):
            return mid_val
           # print(mid_val)
        elif(arr[mid_val]>x):
           return Binary_search(arr,l,mid_val-1,x)
        else:
           return Binary_search(arr,mid_val+1,r,x)
    else:
        return -1
#main()       
arr=array('i',[])
print("Enter the number of array")
n=int(input())
for i in range(0,n):
    arr.append(int(input()))
arr=sorted(arr)
print(arr)
print("Enter the Number for search")
x=int(input())
result=Binary_search(arr,0,n-1,x)
if(result==-1):
    print("Result is not found")
else:
    print("Result is found {}th index".format(result))
