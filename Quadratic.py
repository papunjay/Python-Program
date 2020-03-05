import math
def Quadratic(a,b,c):
    delta=((math.pow(b,2))-(4*a*c))
    if(delta<0):
        print("you not calculate the solution")
    elif(delta==0):
         print(((-b)/2*a))
    else:
        print(((-b)+delta)/2*a)
        print(((-b)-delta)/2*a)
 
a=int(input("Enter the 'a' value"))
b=int(input("enter the 'b' value"))
c=int(input("Enter the 'c' value"))
Quadratic(a,b,c)
