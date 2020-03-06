import sys
import math
from sys import argv
def Euclidean_formula(x_value,y_value):
    k=0
    k= math.sqrt(math.pow(x_value,2) + math.pow(y_value,2))
    return k
    
x_value=int(sys.argv[1])
y_value=int(sys.argv[2])
distance= Euclidean_formula(x_value,y_value)
print(distance) 