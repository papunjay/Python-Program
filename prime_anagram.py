prime_data=[]
def prime_fun(Number_range):
    for Number in range(2,Number_range+1):
        checker=0
        for divider in range(1,Number):
            if(Number%divider==0):
                checker+=1
        if(checker==1):
            prime_data.append(Number)
    return prime_data
    
Number_range=1000
prime_list=prime_fun(Number_range)