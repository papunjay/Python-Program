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

def check_anagram(prime_list):
    ana_list=[]
    for ith in prime_list:
        dist=0
        for jth in prime_list:
            if((ith!=jth )and (sorted(str(ith))==sorted(str(jth)))):
                for index in range(len(ana_list)):
                    if(ith==ana_list[index]):
                        dist+=1
                if(dist==0):
                    ana_list.append(int(ith))
    return ana_list
Number_range=1000
prime_list=prime_fun(Number_range)
anagram_list=check_anagram(prime_list)
TwoDArray=[]
for ren in range(100,1000+1,100):
    oneDArray=[]
    for num in anagram_list:
        if num<= ren and num>=ren-100:
            oneDArray.append(num)
    TwoDArray.append(oneDArray)
for num in TwoDArray:
    print(num)