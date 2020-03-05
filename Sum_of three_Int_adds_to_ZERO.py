from array import *
def triplet_sum(arr,Number):
    count=0
    for i in range(Number-2):
        for j in range(i+1,Number-1):
            for k in range(i+2,Number):
                if(arr[i]+arr[j]+arr[k]==0):
                    count+=1
                    print("{} {} {} ".format(arr[i],arr[j],arr[k]))
    return count

arr=array('i',[])
no_of_triplet=0
print("Enter the Number of Array")
Number=int(input())
for i in range(Number):
    Value=int(input())
    arr.append(Value)
no_of_triplet=triplet_sum(arr,Number)
print(no_of_triplet)