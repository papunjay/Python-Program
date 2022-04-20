def prime_number_fun(number_range):
    p_list=[]
    for Number in range(2,number_range+1):
        check=0
        for divider in range(2,Number):
            if(Number % divider==0):
                check+=1
        if(check==0):
            p_list.append(Number)
    return p_list

number_range=1000
prime_number=prime_number_fun(number_range)

TwoDArray=[]
for ren in range(100,1000+1,100):
    oneDArray=[]
    for num in prime_number:
        if num<= ren and num>=ren-100:
            oneDArray.append(num)
    TwoDArray.append(oneDArray)
for num in TwoDArray:
    print(num)