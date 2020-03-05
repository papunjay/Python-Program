info_data=[]
print("Enter the Row and Cols")
Row=int(input())
col=int(input())
for x in range(Row):
    for y in range(col):
        val=input()
        info_data.append(val)
print(info_data)
