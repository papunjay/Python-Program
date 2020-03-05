print("Entdr the Number")
Number=int(input())
for x in range(2,Number+1):
    count=0
    if(Number%x==0):
        for y in range(2,x+1):
            if(x%y==0):
                count=count+1
        if(count==1):
            print(" {}".format(x))
