count=0
for i in range(2,1000):
    c=0
    for j in range(1,i):
        if(i%j==0):
            c+=1
    if(c==1):
        print(i)   