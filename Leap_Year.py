print("Enter The Year")
Year=int(input())
if(len(str(Year))>=4):
    if((Year%4==0) or (Year%100!=0) and Year%400==0):
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Enter Valid Year")

