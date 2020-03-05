from array import *
arr=array('i',[])
def bubble_sort(arr):
    length=len(arr)
    for i in range(0,length-1):
        for j in range(0,length-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]            
    return arr
#main()
print("Enter the size of Array")
Number=int(input())
for i in range(Number):
    arr.append(int(input()))
print("Entered data")
print(arr)
sort_data=bubble_sort(arr)
print("sort data")
print(arr)