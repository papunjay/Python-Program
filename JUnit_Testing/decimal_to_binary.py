decimal=int(input("Enter the Desimal Number"))
i=0
Binary_data=[]
while(decimal>0):
    if(decimal%2==0):
        Binary_data.append(0)
        decimal=decimal//2
    else:
        Binary_data.append(1)
        decimal=decimal//2

print(Binary_data[::-1])