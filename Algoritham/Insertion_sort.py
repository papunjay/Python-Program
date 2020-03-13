from array import *
arr=array('i',[])
'''def print_data(arr):
    for i in range(0,len(arr)):
        print(arr[i])
'''
def insertion_sort(arr):
    for j in range(1,(len(arr))):
        key=arr[j]
        i=j-1
        while(i>=0 and arr[i]>key):
            arr[i+1]=arr[i]
            i=i-1

        arr[i+1]=key
    return arr
 #main()   
print("Enter the size of Array")
Number=int(input())
for i in range(Number):
    arr.append(int(input()))

print(arr)
sort_data=insertion_sort(arr)
print(arr)