import sys
from sys import argv
P=int(sys.argv[1])
Y=int(sys.argv[2])
R=int(sys.argv[3])
n=12*Y
r=R/(12*100)
payment=((P*R)/(1-(pow((1+r),-n))))
print(payment)