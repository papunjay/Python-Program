
def merge(arr,start_index,mid_index,last_index):
    left_index=0
    right_index=0
    no_of_left_child = mid_index-start_index+1
    no_of_right_child = last_index-mid_index
    left_arr = [no_of_left_child]
    right_arr = [no_of_right_child]
    
    for left_index in range(no_of_left_child):
        left_arr.append(arr[start_index+left_index])
    for right_index in range(no_of_right_child):
        right_arr.append(arr[mid_index+right_index+start_index])

    left_index=0 
    right_index=0
    while(left_index<no_of_left_child and right_index < no_of_right_child):
        if left_arr[left_index]<= right_arr[right_index]:
            arr.append(left_arr[left_index])
            left_index+=1
        else:
            arr.append(right_arr[right_index])
            right_index+=1
    while(left_index < no_of_left_child):
        arr.append(left_arr[left_index])
        left_index+=1
    while(right_index<no_of_right_child):
        arr.append(right_arr[right_index]) 
        right_index+=1
def merge_sort(arr,start_index,last_index):
    if last_index > start_index:
        mid_index=start_index+(last_index-start_index)//2
        merge_sort(arr,start_index,mid_index)
        merge_sort(arr,mid_index+1,start_index)
        merge(arr,start_index,mid_index,last_index)

arr=[]
Number=int(input("Enter the Size of Array\n"))
for arr_index in range(Number):
    arr.append(int(input()))
merge_sort(arr,0,Number-1)
print("Your Entered data is \n 5{}".format(arr))