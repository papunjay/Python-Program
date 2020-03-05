sum_of_value=0
print("Enter The Harmonic Number")
Number=int(input())
for x in range(1,Number+1):
    print (" 1/{}".format(x))
    sum_of_value=sum_of_value+(1/x)
print("{}".format(sum_of_value))