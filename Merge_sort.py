import sys
sys.setrecursionlimit(10**6) 
def merge_sort(arr):
    if len(arr)>1:
        mid_index=len(arr)//2
        left_arr=arr[:mid_index]
        right_arr=arr[mid_index:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        left_index=right_index=arr_index=0
        while(left_index<len(left_arr) and right_index < len(right_arr)):
            if left_arr[left_index]< right_arr[right_index]:
                arr[arr_index]=left_arr[left_index]
                left_index+=1
            else:
                arr[arr_index]=right_arr[right_index]
                right_index+=1
            arr_index+=1
        while(left_index < len(left_arr)):
            arr[arr_index]=left_arr[left_index]
            left_index+=1
        while(right_index<len(right_arr)):
            arr[arr_index]=(right_arr[right_index]) 
            right_index+=1

arr=[]
Number=int(input("Enter the Size of Array\n"))
for arr_index in range(Number):
    arr.append(int(input()))
print("Your Entered data is \n {}".format(arr))
merge_sort(arr)
print(arr)

