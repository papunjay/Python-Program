#prime_number
prime_data=[]
p_string=[]
sort_data=[]
def prime_fun(N):
    for i in range(2,N):
        c=0
        for j in range(1,i):
            if(i%j==0):
                c+=1
        if(c==1):
            prime_data.append(i)
    return prime_data

def anagram(prime_list):
    anagram_list = []
    for i in prime_list: 
        for j in prime_list: 
            if i != j and (sorted(str(i))==sorted(str(j))):
                anagram_list.append(i)
    return anagram_list

def palindrome(prime_list):
    palin_data=[]
    for i in prime_list:
        for j in prime_list:
            if(i!=j and (revers_int(i)==j)):
                palin_data.append(i)
    return palin_data
def revers_int(i):
    rem=0
    rev_no=0
    while (i>0):
        rem=i%10
        rev_no=rev_no*10+rem
        i=i//10
    #print(rev_no)
    return rev_no
if __name__ == '__main__':
    N=1000
    prime_list=prime_fun(N)
    anagram_list=anagram(prime_list)
    palin_list=palindrome(prime_list)
    print("Prime Number...............................")
    print(prime_list)
    print("Anagram Number.............................")
    print(anagram_list)
    print("Palindrome Number...........................")
    print(palin_list)