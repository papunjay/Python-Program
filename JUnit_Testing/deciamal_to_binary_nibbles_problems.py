def decimal_to_binary(decimal): #decimal to binar conversion function
    binary_data=[]
    while(decimal>0):
        if(decimal%2==0):
            binary_data.append(0)
            decimal=decimal//2
        else:
            binary_data.append(1)
            decimal=decimal//2
    return binary_data

def nibbles_swap(binary):
    while(len(binary)< 8): #if length of the binary data is less then 8..we need to add 0
        binary.append(0)
    binary=binary[::-1]
    swap=binary[4:]+binary[:4]
    return swap

def binary_to_decimal(swaped_nibbles):
    dc=0
    i=0
    for val in  swaped_nibbles[::-1]:
        dc=dc+pow(2,i)*val
        i+=1
    return dc
decimal=int(input("Enter the Number"))
binary=decimal_to_binary(decimal) #function which is convert decimal data to binary
print("decimal to Binary data")
print(binary[::-1])
swaped_nibbles=nibbles_swap(binary) #function for nibbles swap
print("After nibbles swap data")
print(swaped_nibbles)
deci=binary_to_decimal(swaped_nibbles)
print("binary to decimal after nibbles swap")
print(deci)